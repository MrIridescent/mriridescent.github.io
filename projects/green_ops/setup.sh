#!/bin/bash

echo "--- Green-Ops Energy Optimizer: 2026 Turnkey Setup ---"
echo ""

# 1. Check Python
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed. Please install it first."
    exit
fi

# 2. Install Dependencies
echo "[1/2] Installing dependencies (requests)..."
pip install requests &> /dev/null
echo ">> Dependencies installed."

# 3. Final Prep
echo "[2/2] Ready to launch!"
echo ""
echo "To run the energy optimization scheduler, use:"
echo "python3 energy_optimizer.py"
echo ""
echo "This will simulate carbon-aware task scheduling and energy reporting."
echo ""
echo "Installation complete."
