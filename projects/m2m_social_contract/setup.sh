#!/bin/bash
# M2M Social Contract Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install blockchain/cryptographic dependencies
sudo apt-get update && sudo apt-get install -y libssl-dev

# 2. Install M2M Negotiation and Smart Contract dependencies
pip install web3 cryptography ecdsa

# 3. Create social contract workspace
mkdir -p ./contracts/legal_templates ./contracts/machine_readable

# 4. Initialize the Social Contract Negotiator
python3 social_contract_negotiator.py

echo "M2M Social Contract Suite Deployed Successfully."
