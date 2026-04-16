#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run tests
pytest test_app.py --headless

# Return exit code based on pytest result
if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi