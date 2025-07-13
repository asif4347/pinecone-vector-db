from pinecone import Pinecone, ServerlessSpec
from config import Config

pc = Pinecone(api_key=Config.PINECONE_API_KEY)
