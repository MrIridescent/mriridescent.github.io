#!/bin/bash
# BOLT DSLM Factory Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install data processing dependencies
sudo apt-get update && sudo apt-get install -y libatlas-base-dev

# 2. Install Knowledge Tree and BOLT dependencies
pip install networkx pandas requests beautifulsoup4

# 3. Create factory workspace
mkdir -p ./data/bronze ./data/silver ./data/gold ./knowledge_trees

# 4. Initialize the BOLT Knowledge Tree Generator
python3 bolt_factory.py

echo "BOLT DSLM Factory Suite Deployed Successfully."
