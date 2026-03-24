#!/bin/bash
# setup.sh - Asset-Flow Liquid-Asset Sovereign Swap (SDG 1 / AU Goal 4)

echo "--- Initializing Asset-Flow Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install aiosqlite asyncio uuid
echo "--- Setup Complete ---"
echo "Run the swap engine with: python3 asset_flow_engine.py"
