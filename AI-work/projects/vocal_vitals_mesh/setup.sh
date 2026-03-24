#!/bin/bash
# 'Cattle-Voice' Vocal-Vitals-Mesh Setup
# Protecting livestock sovereignty through acoustic health AI.

echo "[Cattle-Voice] Initializing the Acoustic Mesh..."

# 1. Setup virtual environment for sound-fusion and anomaly detection
python3 -m venv venv
source venv/bin/activate

# 2. Install the 'Acoustic-Stack'
pip install --upgrade pip
pip install numpy scipy asyncio pydantic-settings librosa

# 3. Configure local Acoustic-Mesh encryption
export HERD_PROTECTION_KEY="SAMBURU-GUARD-$(date +%s)"

# 4. Run the Vocal-Vitals engine to verify the acoustic health loop
python vocal_vitals_engine.py

echo "[Cattle-Voice] Deployment Complete: The Herd is Protected."
