#!/bin/bash
# setup.sh - Orbit-Shield Exo-Sovereign Mesh (AU Goal 10 / SDG 9)

echo "--- Initializing Orbit-Shield Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install numpy asyncio uuid
echo "--- Setup Complete ---"
echo "Run the swarm simulation with: python3 orbit_shield_engine.py"
