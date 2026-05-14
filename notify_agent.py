async def notify(reports):
    return [{
        "notify_to": ["产品A", "运维B"],
        "message": "检测到支付重试策略冲突，请合并文档"
    } for _ in reports]