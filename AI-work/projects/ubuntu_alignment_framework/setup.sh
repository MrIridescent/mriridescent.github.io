#!/bin/bash
# setup.sh - Ubuntu-Alignment Framework (SDG 16 / AU Goal 3)

echo "--- Initializing Ubuntu-Alignment Environment ---"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install essential dependencies for AI Alignment & Consensus logic
echo "Installing dependencies..."
pip install --upgrade pip
pip install numpy asyncio aiosqlite mcp

echo "--- Setup Complete ---"
echo "Run the consensus engine with: python3 ubuntu_consensus_engine.py"
