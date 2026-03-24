#!/bin/bash

echo "--- Edge TinyML Inference Engine: 2026 Turnkey Setup ---"
echo ""

# 1. Check Python
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed. Please install it first."
    exit
fi

# 2. Install Dependencies
echo "[1/2] Installing dependencies (numpy)..."
pip install numpy &> /dev/null
echo ">> Dependencies installed."

# 3. Final Prep
echo "[2/2] Ready to launch!"
echo ""
echo "To run the edge inference simulation, use:"
echo "python3 edge_inference.py"
echo ""
echo "This will simulate model quantization and NPU-based inference."
echo ""
echo "Installation complete."
