#!/bin/bash
# 'Med-Flow-Ledger' Setup
# Verifying medicine authenticity via spectral analysis.

echo "[Med-Flow] Initializing the Integrity Hub..."

# 1. Setup virtual environment for spectral analysis
python3 -m venv venv
source venv/bin/activate

# 2. Install the 'Med-Stack'
pip install --upgrade pip
pip install numpy scipy asyncio pydantic-settings hashlib

# 3. Configure local Med-Mesh encryption
export MED_ENCRYPTION_KEY="FLOW-SOV-$(date +%s)"

# 4. Run the Med-Flow engine to verify the integrity loop
python med_flow_engine.py

echo "[Med-Flow] Deployment Complete: Medicine is Sovereign."
