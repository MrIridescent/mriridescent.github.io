#!/bin/bash
# setup.sh - Nutri-Sovereign Hyper-Local Crop-Spec (SDG 2 / AU Goal 5)

echo "--- Initializing Nutri-Sovereign Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install pandas asyncio
echo "--- Setup Complete ---"
echo "Run the optimizer with: python3 grain_sage_engine.py"
