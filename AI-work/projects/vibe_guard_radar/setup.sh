#!/bin/bash
# 'Vibe-Guard' Setup
# Detecting the 'sound of tension' for peaceful mediation.

echo "[Vibe-Guard] Initializing the Peace Radar..."

# 1. Setup virtual environment for social vibe acoustics
python3 -m venv venv
source venv/bin/activate

# 2. Install the 'Vibe-Stack'
pip install --upgrade pip
pip install numpy scipy asyncio pydantic-settings

# 3. Configure local Vibe-Mesh encryption
export VIBE_ENCRYPTION_KEY="RADAR-SOV-$(date +%s)"

# 4. Run the Vibe-Guard engine to verify the peace-radar loop
python vibe_guard_engine.py

echo "[Vibe-Guard] Deployment Complete: The Vibe is Guarded."
