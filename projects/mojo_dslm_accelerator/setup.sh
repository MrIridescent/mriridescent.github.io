#!/bin/bash
# Mojo DSLM Accelerator Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install Mojo SDK dependencies
sudo apt-get update && sudo apt-get install -y curl build-essential

# 2. Install the Modular CLI (Mojo SDK)
curl https://get.modular.com | sh -

# 3. Setup the Mojo environment
modular auth
modular install mojo

# 4. Verify installation
mojo --version

# 5. Run the Accelerator Implementation
python3 mojo_accelerator.py

echo "Mojo Accelerator Suite Deployed Successfully."
