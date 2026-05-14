# Cross-Document Contradiction Detection Agent MVP

一个面向企业知识库的“跨文档矛盾检测与溯源 Agent”MVP。

## 功能
- 多 Agent 协作
- 文档召回
- 矛盾识别
- 证据链生成
- 自动裁决
- 通知模拟
- React 控制台
- FastAPI 后端

## 技术栈
- Frontend: React + Vite
- Backend: FastAPI
- Queue: AsyncIO
- Agent Orchestration: Python Services

## 启动方式

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## API
- POST /analyze
- GET /health

## 示例请求
```json
{
  "query": "支付超时重试策略"
}
```