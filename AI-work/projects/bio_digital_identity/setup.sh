#!/bin/bash
# Bio-Digital Identity Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install cryptographic dependencies
sudo apt-get update && sudo apt-get install -y libssl-dev

# 2. Install Self-Sovereign Identity (SSI) and biometric dependencies
pip install cryptography pynacl did-resolver-python

# 3. Create identity workspace
mkdir -p ./identity/did_vault ./identity/biometric_encodings

# 4. Initialize the Bio-Digital Identity Core
python3 bio_identity.py

echo "Bio-Digital Identity Suite Deployed Successfully."
