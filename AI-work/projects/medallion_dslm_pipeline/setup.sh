#!/bin/bash
# Medallion DSLM Generation Pipeline Setup Script
# Creator / Programmer: David Akpoviroro Oke (MrIridescent)
# Date: 2026-03-18

echo "--- Medallion DSLM Generation Pipeline 2026 Setup ---"
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
# pip install pyspark delta-spark
echo "Dependencies: JSON Standard Library + Simulated Data Lake API"

echo "Configuring Medallion layer directories..."
mkdir -p data/bronze data/silver data/gold

echo "--- Setup Complete ---"
echo "Run 'python3 medallion_pipeline.py' to start the automated model factory."
