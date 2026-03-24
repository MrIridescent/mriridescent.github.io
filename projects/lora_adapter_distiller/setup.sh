#!/bin/bash
# LoRA Adapter Distiller Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install base dependencies
sudo apt-get update && sudo apt-get install -y git build-essential

# 2. Install Python 3.13 dependencies
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install transformers peft datasets accelerate bitsandbytes

# 3. Create distillation workspace
mkdir -p ./models/teacher ./models/student ./outputs/adapters

# 4. Verify GPU availability
python3 -c "import torch; print(f'GPU Available: {torch.cuda.is_available()}')"

# 5. Run the Distiller Implementation
python3 adapter_distiller.py

echo "LoRA Adapter Distiller Suite Deployed Successfully."
