#!/bin/bash
# Autonomous Admin Intel Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install observability tools
sudo apt-get update && sudo apt-get install -y prometheus prometheus-node-exporter

# 2. Install AIOps and telemetry dependencies
pip install prometheus-client requests scikit-learn

# 3. Create telemetry and self-healing workspace
mkdir -p ./telemetry ./healing_logs

# 4. Initialize the Self-Healing Core
python3 self_healing_core.py

echo "Autonomous Admin Intel Suite Deployed Successfully."
