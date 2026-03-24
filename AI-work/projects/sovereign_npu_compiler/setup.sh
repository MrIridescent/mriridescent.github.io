#!/bin/bash
# setup.sh - Sovereign-NPU-Compiler (SDG 9 / AU Goal 10)

echo "--- Initializing Sovereign-NPU Environment ---"
if [ ! -d "venv" ]; then python3 -m venv venv; fi
source venv/bin/activate
pip install --upgrade pip
pip install onnx asyncio uuid
echo "--- Setup Complete ---"
echo "Run the compiler with: python3 npu_compiler_engine.py"
