#!/bin/bash

echo "--- Psychiatric AI Companion: 2026 Turnkey Setup ---"
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
echo "To run the psychiatric assistant, use:"
echo "python3 psychiatric_companion.py"
echo ""
echo "This will simulate a personality-aware clinical intervention cycle."
echo ""
echo "Installation complete."
