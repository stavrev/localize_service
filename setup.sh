#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it before proceeding."
    exit 1
fi

# Set up a virtual environment
echo "Setting up the virtual environment..."
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found. Skipping dependency installation."
fi

# Check if OPENAI_API_KEY is set
if [ -z "${OPENAI_API_KEY}" ]; then
    echo "Error: The OPENAI_API_KEY environment variable is not set."
    echo "This script requires the OPENAI_API_KEY to be configured for OpenAI API access."
    echo "Please export the variable before proceeding:"
    echo "export OPENAI_API_KEY=<your_api_key>"
    exit 1
fi

# Final message
echo "Setup complete."
