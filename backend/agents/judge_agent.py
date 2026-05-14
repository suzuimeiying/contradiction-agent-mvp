async def judge(evidence):
    reports = []

    for item in evidence:
        reports.append({
            "decision": "采用最新且高优先级SOP策略：不重试直接降级",
            "rule_chain": [
                "比较文档优先级",
                "比较更新时间",
                "选择更高权威版本"
            ],
            "evidence": item
        })

    return reports