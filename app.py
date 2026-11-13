from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="Ollama AI Document Assistant")

MODEL = "llama3.2:3b"

DOCUMENT = """
Company Policy:
Employees receive 15 days of annual leave.
Remote work is allowed 3 days per week.
IT support is available Monday to Friday.
"""

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"status": "running", "model": MODEL}

@app.post("/ask")
def ask(data: Question):
    prompt = f"""Answer only using this document.
If information is missing, say Not found in document.

{DOCUMENT}

Question: {data.question}
"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=120
        )
        response.raise_for_status()
        return {
            "answer": response.json()["response"],
            "source": "Company Policy"
        }
    except requests.RequestException as exc:
        raise HTTPException(status_code=503, detail=str(exc))
