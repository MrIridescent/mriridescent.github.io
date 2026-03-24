#!/bin/bash
# Neuromorphic Edge Core Setup Script
# Creator / Programmer: David Akpoviroro Oke (MrIridescent)
# Date: 2026-03-18

echo "--- Neuromorphic Edge Core 2026 Setup ---"
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
# In a real-world scenario:
# pip install spikingjelly lava-nc
echo "Dependencies: Standard Library + Simulated SNN API"

echo "Configuring local spiking data directories..."
mkdir -p data/sensory_stream data/spike_logs

echo "--- Setup Complete ---"
echo "Run 'python3 neuromorphic_inference.py' to start the spiking simulation."
