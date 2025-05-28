#!/bin/bash
# Quick training script for PII masking models

set -e

echo "🚀 Starting PII Masking Model Training..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies if not already installed
echo "📦 Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1

# Download spaCy models
echo "📥 Downloading spaCy models..."
python -m spacy download en_core_web_sm > /dev/null 2>&1

# Run the main training pipeline
echo "🏋️  Training models..."
jupyter nbconvert --to notebook --execute notebooks/experiments/main.ipynb --output main_executed.ipynb

# Run evaluation
echo "📊 Running evaluation..."
jupyter nbconvert --to notebook --execute notebooks/evaluation/eval.ipynb --output eval_executed.ipynb

echo "✅ Training completed! Check results/ directory for outputs."