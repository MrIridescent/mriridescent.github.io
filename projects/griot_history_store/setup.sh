#!/bin/bash
# 'Griot-History-Store' Setup
# High-dimensional search for indigenous wisdom.

echo "[Griot-Store] Initializing the Wisdom Hub..."

# 1. Setup virtual environment for oral history encoding
python3 -m venv venv
source venv/bin/activate

# 2. Install the 'Griot-Stack'
pip install --upgrade pip
pip install numpy scipy asyncio pydantic-settings hashlib

# 3. Configure local Griot-Mesh encryption
export GRIOT_ENCRYPTION_KEY="STORE-SOV-$(date +%s)"

# 4. Run the Griot-Store engine to verify the wisdom retrieval loop
python griot_engine.py

echo "[Griot-Store] Deployment Complete: Wisdom is Indexed."
