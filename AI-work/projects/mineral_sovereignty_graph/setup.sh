#!/bin/bash
# setup.sh - Mineral-Sovereignty Knowledge Graph (SDG 12 / AU Goal 7)

echo "--- Initializing Mineral-Sovereignty Environment ---"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install essential dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install networkx pandas asyncio numpy

echo "--- Setup Complete ---"
echo "Run the negotiation engine with: python3 mineral_graph_engine.py"
