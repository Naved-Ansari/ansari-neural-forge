from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from agents.orchestrator import orchestrator

app = FastAPI()

# Serve Chat UI
@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r") as f:
        return f.read()

# API Endpoint
@app.post("/query")
def query(data: dict):
    user_input = data.get("input")
    result = orchestrator(user_input)
    return {"response": result}