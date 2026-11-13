# Ollama FastAPI Document Q&A Assistant

A local AI document question-answering API built with Python, FastAPI, Ollama, and Llama 3.2 3B.

## Features
- REST API with FastAPI
- Document-grounded question answering
- Local LLM inference using Ollama
- Source identification
- Interactive Swagger documentation

## Setup
pip install fastapi uvicorn requests

ollama pull llama3.2:3b
python -m uvicorn app:app --reload

## API
POST /ask

Example:
{"question":"How many annual leave days do employees receive?"}

## Tested Result
HTTP 200
Employees receive 15 days of annual leave.

## Next Steps
Azure AI Foundry integration, document upload, retrieval, and evaluation.
