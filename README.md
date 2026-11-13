# Ollama FastAPI AI Document Q&A Assistant

A local AI-powered Document Q&A REST API built with Python, FastAPI, Ollama, and Llama 3.2 3B.

## Features
- AI-powered document question answering
- Local LLM inference with Ollama
- Document-grounded prompting
- Source identification
- FastAPI REST endpoints
- Swagger UI for API testing
- No paid API key required

## Technology Stack
- Python
- FastAPI
- Ollama
- Llama 3.2 3B
- Pydantic
- Requests
- Swagger UI
- Git and GitHub

## Installation

Install dependencies:

    pip install fastapi uvicorn requests

Ensure Ollama is running and the model is installed:

    ollama pull llama3.2:3b

Start the API:

    python -m uvicorn app:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

## Example Request

POST /ask

    {"question": "How many annual leave days do employees receive?"}

## Example Response

    {
      "answer": "Employees receive 15 days of annual leave.",
      "source": "Company Policy"
    }

## Future Enhancements
- Microsoft Foundry integration
- PDF document upload
- Vector search and RAG
- AI evaluation and safety controls

## License
MIT License
