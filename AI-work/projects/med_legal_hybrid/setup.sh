#!/bin/bash
# Med-Legal Hybrid Deployment Script
# Creator: David Akpoviroro Oke (MrIridescent)

# 1. Update system and install text processing dependencies
sudo apt-get update && sudo apt-get install -y tesseract-ocr poppler-utils

# 2. Install Hybrid AI and Med-Legal NLP dependencies
pip install torch transformers pytesseract spacy fuzzywuzzy

# 3. Create med-legal workspace
mkdir -p ./documents/medical_records ./documents/legal_templates

# 4. Initialize the Med-Legal Hybrid Core
python3 med_legal_hybrid.py

echo "Med-Legal Hybrid Suite Deployed Successfully."
