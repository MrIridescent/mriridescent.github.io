#!/bin/bash

echo "--- DSLM Reasoning Engine: 2026 Turnkey Setup ---"
echo ""

# 1. Check Python
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed. Please install it first."
    exit
fi

# 2. Install Dependencies
echo "[1/2] Installing dependencies (pytest for testing)..."
pip install pytest &> /dev/null
echo ">> Dependencies installed."

# 3. Final Prep
echo "[2/2] Ready to launch!"
echo ""
echo "To run the reasoning engine, use:"
echo "python3 reasoning_engine.py"
echo ""
echo "To run the automated tests, use:"
echo "pytest test_reasoning.py"
echo ""
echo "Installation complete."
