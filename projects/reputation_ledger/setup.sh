#!/bin/bash

echo "--- Reputation Ledger: 2026 Turnkey Setup ---"
echo ""

# 1. Check Python
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed. Please install it first."
    exit
fi

# 2. Install Dependencies
echo "[1/2] Installing dependencies (cryptography)..."
pip install cryptography &> /dev/null
echo ">> Dependencies installed."

# 3. Final Prep
echo "[2/2] Ready to launch!"
echo ""
echo "To initialize the reputation ledger, run:"
echo "python3 agent_reputation.py"
echo ""
echo "This will create a verifiable reputation block for a mock agent."
echo ""
echo "Installation complete."
