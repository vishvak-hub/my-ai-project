
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RAGRequest(BaseModel):
    question: str

@app.post("/rag")
def rag_endpoint(request: RAGRequest):
    return {
        "question": request.question,
        "answer": "This is a demo RAG endpoint. Retrieval is not implemented yet."
    }