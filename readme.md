# 🔍 FastAPI + Pinecone Vector Search API

A blazing-fast, production-ready backend API built with [FastAPI](https://fastapi.tiangolo.com/) and [Pinecone](https://www.pinecone.io/) for semantic search and vector-based indexing. This project enables efficient upserting, querying, and health-checking of embeddings using Pinecone's serverless vector database.

> 💡 Ideal for AI applications like RAG (Retrieval-Augmented Generation), semantic search engines, and personalized recommendation systems.

---

## 🚀 Features

- ✅ FastAPI-powered RESTful API
- 🧠 Pinecone vector search & reranking using models like:
  - `llama-text-embed-v2` (embedding)
  - `bge-reranker-v2-m3` (reranking)
- 📅 Upsert multiple documents with metadata (category, chunked text, etc.)
- 🔍 Query similar vectors with reranking
- 📊 Health check and index statistics
- ⚙️ Environment-configurable for flexible deployment

---

## 📦 Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Vector DB**: [Pinecone Serverless](https://docs.pinecone.io/docs/serverless-intro)
- **Env Config**: `python-dotenv`
- **Async Support**: Full `async` FastAPI architecture

---

## 📁 Project Structure

```
.
├── main.py                  # FastAPI entry point
├── pine_cone/
│   └── utils.py             # Pinecone index utilities (upsert, search, stats)
├── training/
│   └── records.py           # Sample training records for upserting
├── config.py                # Configuration loader using environment variables
├── .env                     # Local environment variables
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone  https://github.com/asif4347/pinecone-vector-db.git
cd pinecone-vector-db
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root:

```env
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_INDEX=your-index-name
PINECONE_NAMESPACE=your-namespace-name
```

---

## 🧪 Running the App

```bash
uvicorn main:app --reload
```

API will be accessible at: [http://localhost:8000](http://localhost:8000)

---

## 📡 API Endpoints

| Method | Endpoint               | Description                      |
| ------ | ---------------------- | -------------------------------- |
| GET    | `/api`                 | Base route                       |
| GET    | `/api/hello/{name}`    | Hello test route                 |
| GET    | `/api/pinecone/search` | Search query: `?query=...`       |
| GET    | `/api/pinecone/upsert` | Upsert documents into the index  |
| GET    | `/api/pinecone/health` | View Pinecone index health/stats |

---

## 📊 Example Search Response

```json
{
  "results": {
    "result": {
      "hits": [
        {
          "_id": "doc1",
          "_score": 0.98,
          "fields": {
            "chunk_text": "Example chunk text...",
            "category": "education"
          }
        }
      ]
    }
  }
}
```

---

## ✍️ Contributing

We welcome contributions! Here’s how to get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to your branch: `git push origin feature-name`
5. Open a pull request

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- [FastAPI](https://github.com/tiangolo/fastapi)
- [Pinecone](https://www.pinecone.io/)
- [OpenAI Embedding Models](https://platform.openai.com/docs/guides/embeddings)

---

## 💬 Questions or Support?

Open an [Issue](https://github.com/asif4347/pinecone-vector-db/issues) or reach out at `moh.asif4347@gmail.com`.

---

### ⭐️ Give this repo a star if it helped you!

