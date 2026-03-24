#!/bin/bash
# setup.sh - Hydro-Sovereign Molecular Auditor (SDG 6 / AU Goal 1)

echo "--- Initializing Hydro-Sovereign Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install numpy asyncio uuid
echo "--- Setup Complete ---"
echo "Run the auditor with: python3 hydro_auditor_engine.py"
