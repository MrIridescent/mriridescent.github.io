#!/bin/bash
# setup.sh - Indaba-Oracle Restorative-Justice Mediator (SDG 16 / AU Goal 13)

echo "--- Initializing Indaba-Oracle Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install transformers asyncio uuid
echo "--- Setup Complete ---"
echo "Run the mediator with: python3 indaba_mediator_engine.py"
