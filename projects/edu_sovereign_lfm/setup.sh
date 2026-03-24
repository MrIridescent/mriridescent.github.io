#!/bin/bash
# setup.sh - Edu-Sovereign Low-Resource LFM (SDG 4 / AU Goal 2)

echo "--- Initializing Edu-Sovereign Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install transformers asyncio
echo "--- Setup Complete ---"
echo "Run the tutor with: python3 lingo_lift_engine.py"
