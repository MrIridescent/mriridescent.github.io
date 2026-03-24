#!/bin/bash
# Bio-Finance Engine Setup Script
# Creator / Programmer: David Akpoviroro Oke (MrIridescent)
# Date: 2026-03-18

echo "--- Bio-Finance Engine 2026 Setup ---"
echo "Project by David Akpoviroro Oke (MrIridescent)"

# Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "Error: python3 is not installed. Please install Python 3.10+."
    exit 1
fi

echo "Initializing Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing core dependencies (Mock Simulation Mode)..."
# In a real-world scenario, you would install packages like:
# pip install ray mcp tensorflow-lite-micro-python
echo "Dependencies: Standard Library + Simulated MCP Interface"

echo "Configuring secure data directories..."
mkdir -p data/clinical_trials data/market_projections

echo "--- Setup Complete ---"
echo "Run 'python3 bio_finance_engine.py' to start the analysis engine."
