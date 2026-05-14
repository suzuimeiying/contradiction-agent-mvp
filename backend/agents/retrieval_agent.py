from sample_docs import DOCUMENTS

async def retrieve(query: str):
    return [doc for doc in DOCUMENTS if "支付" in query]