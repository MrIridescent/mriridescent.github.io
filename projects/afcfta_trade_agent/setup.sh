#!/bin/bash
# setup.sh - AfCFTA Trade-Agent (SDG 1 / AU Goal 4)

echo "--- Initializing AfCFTA Trade-Agent Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install aiosqlite asyncio uuid
echo "--- Setup Complete ---"
echo "Run the trade agent with: python3 trade_agent_engine.py"
