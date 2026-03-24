#!/bin/bash
# setup.sh - Agri-Bot VLA (SDG 9 / AU Goal 1)

echo "--- Initializing Agri-Bot Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install numpy asyncio pybullet uuid
echo "--- Setup Complete ---"
echo "Run the harvest simulation with: python3 agri_bot_engine.py"
