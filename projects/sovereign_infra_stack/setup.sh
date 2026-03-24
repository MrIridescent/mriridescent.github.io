#!/bin/bash
# Sovereign Infra Stack Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install infrastructure orchestration dependencies
sudo apt-get update && sudo apt-get install -y terraform ansible

# 2. Install Sovereign Cloud and Kubernetes dependencies
pip install kubernetes hcloud python-terraform

# 3. Create infrastructure workspace
mkdir -p ./infrastructure/terraform ./infrastructure/ansible

# 4. Initialize the Sovereign Infra Core
python3 sovereign_infra.py

echo "Sovereign Infra Stack Suite Deployed Successfully."
