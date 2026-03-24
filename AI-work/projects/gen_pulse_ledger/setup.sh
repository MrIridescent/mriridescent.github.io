#!/bin/bash
# setup.sh - Gen-Pulse Bio-Digital Genomic Ledger (SDG 3 / AU Goal 6)

echo "--- Initializing Gen-Pulse Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install cryptography asyncio uuid
echo "--- Setup Complete ---"
echo "Run the discovery engine with: python3 gen_pulse_engine.py"
