#!/bin/bash

echo "--- A2A Commerce & Bidding: 2026 Turnkey Setup ---"
echo ""

# 1. Check Python
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed. Please install it first."
    exit
fi

# 2. Final Prep
echo "[1/1] Ready to launch!"
echo ""
echo "To run the bidding engine, use:"
echo "python3 bidding_engine.py"
echo ""
echo "This will simulate an autonomous auction between multiple agents."
echo ""
echo "Installation complete."
