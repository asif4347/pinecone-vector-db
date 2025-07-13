from pinecone import Pinecone, ServerlessSpec
from config import Config
import time

pc = Pinecone(api_key=Config.PINECONE_API_KEY)
namespace = Config.PINECONE_NAMESPACE


def get_or_create_index(index_name):
    """
    Get or create pinecone index
    :param index_name:
    :return: Dense index
    """

    if not pc.has_index(index_name):
        pc.create_index_for_model(
            name=index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model": "llama-text-embed-v2",
                "field_map": {"text": "chunk_text"}
            }
        )
    return pc.Index(index_name)


def upsert_index_records(index_name, records):
    """
    Upsert namespace records
    :param index_name:
    :param records:

    :return:
    """
    dense_index = get_or_create_index(index_name)
    dense_index.upsert_records(namespace=namespace, records=records)


def check_status(index_name):
    dense_index = get_or_create_index(index_name)
    # time.sleep(10)

    # View stats for the index
    stats = dense_index.describe_index_stats()
    print(stats)
    return stats


def search(index_name, query, top_k=10, top_n=10):
    """
    Search the dense index and rerank results
    :param index_name:
    :param query:
    :param top_k
    :param top_n
    :return:
    """

    dense_index = get_or_create_index(index_name)
    reranked_results = dense_index.search(
        namespace=namespace,
        query={
            "top_k": top_k,
            "inputs": {
                'text': query
            }
        },
        rerank={
            "model": "bge-reranker-v2-m3",
            "top_n": top_n,
            "rank_fields": ["chunk_text"]
        }
    )

    # Print the reranked results
    for hit in reranked_results['result']['hits']:
        print(
            f"id: {hit['_id']}, score: {round(hit['_score'], 2)}, text: {hit['fields']['chunk_text']}, category: {hit['fields']['category']}")

    return reranked_results
