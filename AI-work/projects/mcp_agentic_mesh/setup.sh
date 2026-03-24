#!/bin/bash

echo "--- MCP Agentic Mesh: 2026 Turnkey Setup ---"
echo ""

# 1. Check Python
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed. Please install it first."
    exit
fi

# 2. Install Dependencies
echo "[1/3] Installing dependencies..."
pip install fastapi uvicorn pydantic sqlalchemy requests &> /dev/null
echo ">> Dependencies installed."

# 3. Initialize Database (Handled by server.py on startup)
echo "[2/3] Preparing SQLite knowledge base..."
# No action needed, SQLite is auto-created.

# 4. Start Server (Background)
echo "[3/3] Ready to launch!"
echo ""
echo "To start the server, run:"
echo "python3 server.py"
echo ""
echo "To test with a client, use API Key: sk-2026-strategic-mcp-key"
echo ""
echo "Installation complete."
