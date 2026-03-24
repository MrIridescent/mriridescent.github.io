#!/bin/bash

echo "--- Federated Intelligence Hub: 2026 Turnkey Setup ---"
echo ""

# 1. Check Python
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed. Please install it first."
    exit
fi

# 2. Install Dependencies
echo "[1/2] Installing dependencies (fastapi, numpy, uvicorn)..."
pip install fastapi numpy uvicorn requests &> /dev/null
echo ">> Dependencies installed."

# 3. Final Prep
echo "[2/2] Ready to launch!"
echo ""
echo "To start the federation server, run:"
echo "python3 server.py"
echo ""
echo "The server will listen on port 8000 for decentralized weight updates."
echo ""
echo "Installation complete."
