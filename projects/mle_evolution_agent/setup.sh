#!/bin/bash
# MLE Evolution Agent Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install AutoML dependencies
sudo apt-get update && sudo apt-get install -y libatlas-base-dev

# 2. Install MLE Agent and Self-Evolving AI dependencies
pip install torch optuna scikit-learn hyperopt

# 3. Create evolution workspace
mkdir -p ./evolution/hypotheses ./evolution/checkpoints

# 4. Initialize the MLE Evolution Agent
python3 mle_agent.py

echo "MLE Evolution Agent Suite Deployed Successfully."
