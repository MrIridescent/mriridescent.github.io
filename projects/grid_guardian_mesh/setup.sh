#!/bin/bash
# setup.sh - Grid-Guardian Self-Healing Sovereign Grid (SDG 7 / AU Goal 10)

echo "--- Initializing Grid-Guardian Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install numpy asyncio uuid
echo "--- Setup Complete ---"
echo "Run the grid agent with: python3 grid_guardian_engine.py"
