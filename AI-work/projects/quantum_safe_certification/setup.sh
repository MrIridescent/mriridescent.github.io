#!/bin/bash
# Quantum-Safe Certification Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install post-quantum cryptographic dependencies
sudo apt-get update && sudo apt-get install -y liboqs-dev

# 2. Install PQC and Quantum-Safe Audit dependencies
pip install oqs cryptography pynacl

# 3. Create certification workspace
mkdir -p ./certification/lattice_keys ./certification/audit_logs

# 4. Initialize the Quantum-Safe Auditor
python3 quantum_safe_audit.py

echo "Quantum-Safe Certification Suite Deployed Successfully."
