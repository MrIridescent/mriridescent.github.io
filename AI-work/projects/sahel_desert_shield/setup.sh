#!/bin/bash
# setup.sh - Sahel-Desert-Shield (SDG 15 / AU Goal 1)

echo "--- Initializing Sahel-Desert-Shield Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install numpy asyncio uuid
echo "--- Setup Complete ---"
echo "Run the sentinel simulation with: python3 sand_sentinel_engine.py"
