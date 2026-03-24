#!/bin/bash
# Reasoning Distillation Factory Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install distillation dependencies
sudo apt-get update && sudo apt-get install -y libatlas-base-dev

# 2. Install CoT and Reasoning Distillation dependencies
pip install torch transformers datasets accelerate bitsandbytes

# 3. Create distillation workspace
mkdir -p ./distillation/teacher_cot ./distillation/student_models

# 4. Initialize the Distillation Engine
python3 distillation_engine.py

echo "Reasoning Distillation Factory Suite Deployed Successfully."
