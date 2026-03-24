#!/bin/bash
# FATE-LLM Federated Trainer Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install base dependencies
sudo apt-get update && sudo apt-get install -y git build-essential curl

# 2. Install FATE-LLM and its dependencies
pip install fate fate-llm
pip install ray[default] torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# 3. Initialize FATE environment
mkdir -p ./data/local ./outputs/weights ./logs
fate board init --coordinator_ip 127.0.0.1

# 4. Verify FATE connectivity
python3 -c "import fate; print('FATE Library Loaded Successfully.')"

# 5. Run the Federated Trainer Implementation
python3 fate_federated_trainer.py

echo "FATE-LLM Federated Trainer Suite Deployed Successfully."
