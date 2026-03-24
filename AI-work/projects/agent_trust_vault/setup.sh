#!/bin/bash
# Agent Trust Vault Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install dependencies
sudo apt-get update && sudo apt-get install -y python3-pip

# 2. Install cryptographic and P2P dependencies
pip install cryptography pynacl

# 3. Create vault workspace
mkdir -p ./vault/keys ./vault/reputation_logs

# 4. Initialize the Reputation Vault
python3 reputation_vault.py

echo "Agent Trust Vault Suite Deployed Successfully."
