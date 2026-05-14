from agents.retrieval_agent import retrieve
from agents.contradiction_agent import detect_contradictions
from agents.evidence_agent import build_evidence
from agents.judge_agent import judge
from agents.notify_agent import notify

async def run_pipeline(query: str):
    docs = await retrieve(query)
    contradictions = await detect_contradictions(docs)
    evidence = await build_evidence(contradictions)
    reports = await judge(evidence)
    notifications = await notify(reports)

    return {
        "query": query,
        "documents": docs,
        "contradictions": contradictions,
        "reports": reports,
        "notifications": notifications
    }