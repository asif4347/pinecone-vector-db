from fastapi import FastAPI
from fastapi.responses import JSONResponse

from pine_cone import utils as pinecone_utils
from config import Config
from training.records import records

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/pinecone/search")
async def pinecone_search(query: str):
    try:
        results = pinecone_utils.search(index_name=Config.PINECONE_INDEX,
                                        query=query,
                                        top_k=5)
        # print(f"Search results for query '{query}': {results}")
        return JSONResponse(content={"results": results.to_dict()})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/pinecone/upsert")
async def pinecone_upsert():
    try:
        pinecone_utils.upsert_index_records(Config.PINECONE_INDEX, records)

        return JSONResponse(content={"message": "Data upserted successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/pinecone/health")
async def pinecone_health():
    try:
        health_status = pinecone_utils.check_status(Config.PINECONE_INDEX)
        return JSONResponse(content={"health": health_status.to_dict()})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
