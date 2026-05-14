async def build_evidence(contradictions):
    evidence = []

    for item in contradictions:
        evidence.append({
            "evidence": [
                item["doc_a"]["content"],
                item["doc_b"]["content"]
            ],
            "meta": {
                "doc_a_author": item["doc_a"]["author"],
                "doc_b_author": item["doc_b"]["author"]
            },
            "reason": item["reason"]
        })

    return evidence