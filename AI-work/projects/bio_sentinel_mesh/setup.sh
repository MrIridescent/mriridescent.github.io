#!/bin/bash
# setup.sh - Bio-Sentinel Carbon Mesh (SDG 15 / AU Goal 1)

echo "--- Initializing Bio-Sentinel Carbon Mesh Environment ---"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install essential dependencies for TinyML simulation and soil modeling
echo "Installing dependencies..."
pip install --upgrade pip
pip install numpy scipy asyncio uuid

echo "--- Setup Complete ---"
echo "Run the sentinel simulation with: python3 bio_sentinel_engine.py"
