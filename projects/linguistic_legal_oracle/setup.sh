#!/bin/bash
# setup.sh - Linguistic-Legal-Oracle (SDG 10 / AU Goal 3)

echo "--- Initializing Linguistic-Legal-Oracle Environment ---"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install essential dependencies for NLP and Blockchain-ready anchors
echo "Installing dependencies..."
pip install --upgrade pip
pip install transformers torch asyncio uuid

echo "--- Setup Complete ---"
echo "Run the oracle engine with: python3 legal_oracle_engine.py"
