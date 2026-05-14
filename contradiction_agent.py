async def detect_contradictions(docs):
    contradictions = []

    for i in range(len(docs)):
        for j in range(i + 1, len(docs)):
            a = docs[i]
            b = docs[j]

            if ("重试3次" in a["content"] and "不重试" in b["content"]) or                ("不重试" in a["content"] and "重试3次" in b["content"]):
                contradictions.append({
                    "doc_a": a,
                    "doc_b": b,
                    "reason": "重试策略冲突"
                })

    return contradictions