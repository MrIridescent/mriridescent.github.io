#!/bin/bash
# Supply Chain Diplomacy Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install graph processing dependencies
sudo apt-get update && sudo apt-get install -y libatlas-base-dev

# 2. Install Knowledge Graph and Diplomacy AI dependencies
pip install networkx pandas matplotlib requests

# 3. Create diplomacy workspace
mkdir -p ./graphs/global_supply ./graphs/geopolitical_nodes

# 4. Initialize the Diplomacy Graph Engine
python3 diplomacy_graph.py

echo "Supply Chain Diplomacy Suite Deployed Successfully."
