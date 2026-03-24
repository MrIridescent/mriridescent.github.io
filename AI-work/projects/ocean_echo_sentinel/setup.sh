#!/bin/bash
# setup.sh - Ocean-Echo Blue-Sovereign Acoustic Sentinel (SDG 14 / AU Goal 6)

echo "--- Initializing Ocean-Echo Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install numpy asyncio uuid
echo "--- Setup Complete ---"
echo "Run the sentinel simulation with: python3 ocean_echo_engine.py"
