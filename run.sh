#!/bin/bash

# Exit immediately if any command fails
set -e

# Check if the config file is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: ./run.sh <path_to_config_file>"
    exit 1
fi

CONFIG_FILE=$1

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup.sh..."
    if [ -f "./setup.sh" ]; then
        ./setup.sh
    else
        echo "Error: setup.sh script not found."
        exit 1
    fi
fi

# Check if OPENAI_API_KEY is set
if [ -z "${OPENAI_API_KEY}" ]; then
    echo "Error: The OPENAI_API_KEY environment variable is not set."
    echo "The script cannot run without this variable configured."
    exit 1
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Run the Python script
echo "Running the Python script with config: $CONFIG_FILE"
python3 src/main.py "$CONFIG_FILE"

# Deactivate the virtual environment
deactivate
