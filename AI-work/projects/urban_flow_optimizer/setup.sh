#!/bin/bash
# setup.sh - Urban-Flow-Optimizer (SDG 11 / AU Goal 10)

echo "--- Initializing Urban-Flow-Optimizer Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install networkx asyncio uuid
echo "--- Setup Complete ---"
echo "Run the optimizer with: python3 urban_flow_engine.py"
