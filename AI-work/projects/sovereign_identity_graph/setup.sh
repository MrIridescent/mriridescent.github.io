#!/bin/bash
# 'Afro-ID' Sovereign Graph Setup
# Deploying the privacy-preserving self-sovereign identity (SSI) and ZKP engine.

echo "[Afro-ID] Initializing the Identity Hub..."

# 1. Setup the virtual environment for SSI and cryptographic verification
python3 -m venv venv
source venv/bin/activate

# 2. Install the 'Identity-Stack'
# Using common scientific and web3 libraries
pip install --upgrade pip
pip install numpy scipy asyncio pydantic-settings web3 cryptography

# 3. Configure local DID-Mesh encryption (Mocked as an environment variable)
export IDENTITY_ENCRYPTION_KEY="SSI-PROTECT-$(date +%s)"

# 4. Run the Identity-Graph engine to verify the registration and verification loop
python identity_graph_engine.py

echo "[Afro-ID] Deployment Complete: Your Identity is Yours."
