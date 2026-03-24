from fastapi import FastAPI, HTTPException, Depends, Security, Request, WebSocket, WebSocketDisconnect
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings
from typing import List, Dict, Any, Optional, Union
import uuid
import datetime
import logging
import psutil
import json
import asyncio
from databases import Database
import sqlalchemy
from sqlalchemy import MetaData, Table, Column, Integer, String, Text, DateTime
from collections import deque
import time

# 1. Production Settings (Environment-Aware)
class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./mcp_knowledge.db"
    API_KEY: str = "sk-2026-strategic-mcp-key"
    MCP_PROTOCOL_VERSION: str = "1.2.0" # Upgraded version
    SERVER_ID: str = f"mcp-node-{uuid.uuid4().hex[:8]}"
    RATE_LIMIT_CPM: int = 100 # Calls Per Minute

    class Config:
        env_file = ".env"

settings = Settings()

# 2. Database Layer (Async with Databases/SQLAlchemy)
metadata = MetaData()
research_table = Table(
    "research",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("topic", String(100), unique=True, index=True),
    Column("content", Text),
    Column("last_updated", DateTime, default=datetime.datetime.utcnow),
)

# New: Audit Table for Traceability
audit_table = Table(
    "audit_logs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("request_id", String(50)),
    Column("method", String(50)),
    Column("params", Text),
    Column("timestamp", DateTime, default=datetime.datetime.utcnow),
    Column("status", String(20)),
)

# New: Agent State Table
state_table = Table(
    "agent_state",
    metadata,
    Column("agent_id", String(50), primary_key=True),
    Column("state_json", Text),
    Column("last_modified", DateTime, default=datetime.datetime.utcnow),
)

database = Database(settings.DATABASE_URL)

# 3. Schema Definitions
class JsonRpcRequest(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    params: Dict[str, Any] = {}
    id: Optional[Union[str, int]] = None

class JsonRpcResponse(BaseModel):
    jsonrpc: str = "2.0"
    result: Optional[Any] = None
    error: Optional[Dict[str, Any]] = None
    id: Optional[Union[str, int]] = None

# 4. App Initialization
app = FastAPI(
    title="High-Performance Agentic MCP 2026 Node (v1.2)",
    description="Universal adapter for the 2026 Agentic Ecosystem with Orchestration, Audit, and State management.",
)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("MCP-Prod")

api_key_header = APIKeyHeader(name="X-MCP-API-KEY")

# Simple Rate Limiter (Token Bucket)
class RateLimiter:
    def __init__(self, limit: int):
        self.limit = limit
        self.calls = deque()

    def check(self):
        now = time.time()
        while self.calls and self.calls[0] < now - 60:
            self.calls.popleft()
        if len(self.calls) >= self.limit:
            return False
        self.calls.append(now)
        return True

limiter = RateLimiter(settings.RATE_LIMIT_CPM)

async def get_api_key(api_key: str = Security(api_key_header)):
    if not limiter.check():
        raise HTTPException(status_code=429, detail="Rate Limit Exceeded (100 CPM)")
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail={"code": -32001, "message": "Access Denied: Invalid Agent Token"})
    return api_key

@app.on_event("startup")
async def startup():
    await database.connect()
    engine = sqlalchemy.create_engine(settings.DATABASE_URL.replace("+aiosqlite", ""))
    metadata.create_all(engine)
    
    # Seed if empty
    query = research_table.select()
    rows = await database.fetch_all(query)
    if not rows:
        logger.info("Seeding production knowledge base...")
        seed_data = [
            {"topic": "DSLM", "content": "2026 standard for high-precision specialization via neuro-symbolic refinement."},
            {"topic": "MCP", "content": "Universal Model Context Protocol (JSON-RPC 2.0) for M2M orchestration."},
            {"topic": "SOVEREIGN-AI", "content": "Localized infrastructure for non-custodial intelligence management."}
        ]
        query = research_table.insert()
        await database.execute_many(query, seed_data)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# 5. Core MCP Logic (V1.2 with Orchestration)
class MCPController:
    tools_registry = [
        {"name": "research.query", "description": "Query specialized knowledge base.", "params": ["topic"]},
        {"name": "system.metrics", "description": "Get real-time system/NPU health.", "params": []},
        {"name": "agent.get_state", "description": "Retrieve persisted agent state.", "params": ["agent_id"]},
        {"name": "agent.set_state", "description": "Persist agent state for cross-session memory.", "params": ["agent_id", "state"]},
        {"name": "mcp.orchestrate", "description": "Run complex multi-tool workflows.", "params": ["plan"]}
    ]

    @classmethod
    async def handle_rpc(cls, request: JsonRpcRequest):
        method = request.method
        params = request.params
        req_id = request.id

        try:
            # Audit Log Entry
            await database.execute(audit_table.insert(), {
                "request_id": str(req_id), "method": method, 
                "params": json.dumps(params), "status": "PENDING"
            })

            if method == "mcp.initialize":
                result = {
                    "protocol_version": settings.MCP_PROTOCOL_VERSION,
                    "server_id": settings.SERVER_ID,
                    "capabilities": {"tools": True, "resources": True, "state": True, "orchestration": True}
                }

            elif method == "mcp.list_tools":
                result = {"tools": cls.tools_registry}

            elif method == "research.query":
                topic = params.get("topic", "").upper()
                query = research_table.select().where(research_table.c.topic.ilike(f"%{topic}%"))
                entry = await database.fetch_one(query)
                if not entry:
                    result = {"error": "Topic not found"}
                else:
                    result = {"content": entry["content"], "last_updated": str(entry["last_updated"])}

            elif method == "system.metrics":
                result = {
                    "cpu": psutil.cpu_percent(), "mem": psutil.virtual_memory().percent,
                    "npu_simulated_tops": 700.0, "status": "OPERATIONAL"
                }

            elif method == "agent.get_state":
                agent_id = params.get("agent_id")
                query = state_table.select().where(state_table.c.agent_id == agent_id)
                row = await database.fetch_one(query)
                result = json.loads(row["state_json"]) if row else {}

            elif method == "agent.set_state":
                agent_id = params.get("agent_id")
                state = params.get("state")
                query = state_table.insert().values(agent_id=agent_id, state_json=json.dumps(state)).on_conflict_do_update(
                    index_elements=["agent_id"], set_={"state_json": json.dumps(state), "last_modified": datetime.datetime.utcnow()}
                )
                # SQLite-compatible Upsert logic for databases lib
                existing = await database.fetch_one(state_table.select().where(state_table.c.agent_id == agent_id))
                if existing:
                    await database.execute(state_table.update().where(state_table.c.agent_id == agent_id).values(state_json=json.dumps(state)))
                else:
                    await database.execute(state_table.insert().values(agent_id=agent_id, state_json=json.dumps(state)))
                result = {"status": "success"}

            # V1.2 FEATURE: Orchestration
            elif method == "mcp.orchestrate":
                plan = params.get("plan", []) # List of steps {method, params}
                results = []
                for step in plan:
                    step_req = JsonRpcRequest(method=step["method"], params=step["params"], id=f"step-{uuid.uuid4().hex[:4]}")
                    step_resp = await cls.handle_rpc(step_req)
                    results.append({"step": step["method"], "result": step_resp.result, "error": step_resp.error})
                result = {"steps": results}

            else:
                return JsonRpcResponse(id=req_id, error={"code": -32601, "message": "Method not found"})

            # Update Audit Log to SUCCESS
            await database.execute(audit_table.update().where(audit_table.c.request_id == str(req_id)).values(status="SUCCESS"))
            return JsonRpcResponse(id=req_id, result=result)

        except Exception as e:
            logger.error(f"Execution Error: {str(e)}")
            await database.execute(audit_table.update().where(audit_table.c.request_id == str(req_id)).values(status="ERROR"))
            return JsonRpcResponse(id=req_id, error={"code": -32000, "message": f"Server Error: {str(e)}"})

@app.post("/mcp/v1/rpc", response_model=JsonRpcResponse)
async def http_rpc(request: JsonRpcRequest, auth: str = Depends(get_api_key)):
    return await MCPController.handle_rpc(request)

@app.websocket("/mcp/v1/ws")
async def websocket_rpc(websocket: WebSocket):
    await websocket.accept()
    logger.info(f"WebSocket Connection: {websocket.client}")
    try:
        while True:
            data = await websocket.receive_text()
            try:
                raw_req = json.loads(data)
                req = JsonRpcRequest(**raw_req)
                response = await MCPController.handle_rpc(req)
                await websocket.send_text(response.model_dump_json())
            except Exception as e:
                await websocket.send_text(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}, "id": None}))
    except WebSocketDisconnect:
        logger.info("WebSocket Disconnected")

@app.get("/health")
async def health():
    return {"status": "UP", "server_id": settings.SERVER_ID, "database": "CONNECTED" if database.is_connected else "DISCONNECTED"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
