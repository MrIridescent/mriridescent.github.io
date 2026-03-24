#!/bin/bash
# Green TinyML CI/CD Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install energy profiling tools
sudo apt-get update && sudo apt-get install -y prometheus-node-exporter

# 2. Install Scaphandre and Green Metrics dependencies
pip install scaphandre prometheus-client requests

# 3. Create CI/CD and energy profiling workspace
mkdir -p ./cicd/artifacts ./energy_reports

# 4. Initialize the Green Energy Profiler
python3 energy_profiler.py

echo "Green TinyML CI/CD Suite Deployed Successfully."
