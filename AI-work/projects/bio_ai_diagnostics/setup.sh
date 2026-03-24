#!/bin/bash
# Bio-AI Diagnostics Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install signal processing dependencies
sudo apt-get update && sudo apt-get install -y libatlas-base-dev

# 2. Install Bio-AI and TinyML dependencies
pip install numpy scipy scikit-learn tensorflow-lite

# 3. Create diagnostics workspace
mkdir -p ./clinical_data ./models/embedded

# 4. Initialize the Embedded Bio-AI Diagnostic Core
python3 embedded_bio_ai.py

echo "Bio-AI Diagnostics Suite Deployed Successfully."
