#!/usr/bin/env python3
"""
Setup script for PII Masking project.
Quick setup and installation helper.
"""

import subprocess
import sys
import os

def install_requirements():
    """Install Python requirements."""
    print("Installing Python requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def download_spacy_models():
    """Download required spaCy models."""
    print("Downloading spaCy models...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_lg"])
        print("Large model downloaded successfully!")
    except subprocess.CalledProcessError:
        print("Large model download failed - continuing with small model")

def create_env_file():
    """Create environment file template."""
    env_content = """# AWS Configuration (optional)
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_DEFAULT_REGION=us-east-1

# Project Configuration
PROJECT_ROOT=/home/morrisubuntu/Desktop/SCH_PII_masking_Advanced_ML
"""
    
    if not os.path.exists('.env'):
        with open('.env.example', 'w') as f:
            f.write(env_content)
        print("Created .env.example - copy to .env and configure as needed")

def main():
    """Main setup function."""
    print("Setting up PII Masking project...")
    
    try:
        install_requirements()
        download_spacy_models()
        create_env_file()
        print("\n✅ Setup completed successfully!")
        print("Next steps:")
        print("1. Configure .env file if using AWS")
        print("2. Run: jupyter notebook notebooks/experiments/main.ipynb")
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()