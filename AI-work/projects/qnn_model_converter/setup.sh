#!/bin/bash
# Qualcomm QNN Converter Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install cross-compilation dependencies
sudo apt-get update && sudo apt-get install -y git build-essential gcc-aarch64-linux-gnu g++-aarch64-linux-gnu

# 2. Setup the Qualcomm AI Stack environment
# NOTE: In a real environment, you must download the Qualcomm AI Stack SDK from their portal.
mkdir -p ./qnn_sdk/bin ./qnn_sdk/lib ./qnn_sdk/include
export QNN_SDK_ROOT=$(pwd)/qnn_sdk
export PATH=$QNN_SDK_ROOT/bin:$PATH
export LD_LIBRARY_PATH=$QNN_SDK_ROOT/lib:$LD_LIBRARY_PATH

# 3. Install Python dependencies for model export
pip install torch onnx onnxruntime

# 4. Create build workspace
mkdir -p ./models ./build/qnn_context ./deploy

# 5. Run the QNN Converter Implementation
python3 qnn_converter.py

echo "Qualcomm QNN Converter Suite Deployed Successfully."
