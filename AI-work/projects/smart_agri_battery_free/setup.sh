#!/bin/bash
# Smart Agriculture: Battery-Free TinyML Setup Script
# Creator / Programmer: David Akpoviroro Oke (MrIridescent)
# Date: 2026-03-18

echo "--- Smart Agriculture Battery-Free TinyML 2026 Setup ---"
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
# pip install tflite-micro-python
echo "Dependencies: Standard Library + Simulated Harvester API"

echo "Configuring local sensor log directories..."
mkdir -p logs/telemetry logs/energy_status

echo "--- Setup Complete ---"
echo "Run 'python3 battery_free_agri.py' to start the soil sensor simulation."
