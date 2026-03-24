#!/bin/bash
# Exo-Space Autonomy Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install aerospace simulation dependencies
sudo apt-get update && sudo apt-get install -y libatlas-base-dev

# 2. Install Neuromorphic and Space AI dependencies
pip install numpy scipy astropy lava-dl

# 3. Create deep-space workspace
mkdir -p ./telemetry/deep_space ./models/neuromorphic

# 4. Initialize the Space Autonomy Engine
python3 space_autonomy.py

echo "Exo-Space Autonomy Suite Deployed Successfully."
