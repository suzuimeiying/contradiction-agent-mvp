from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator import run_pipeline

app = FastAPI(title="Contradiction Agent MVP")

class AnalyzeRequest(BaseModel):
    query: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    result = await run_pipeline(req.query)
    return result