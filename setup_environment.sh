#!/bin/bash

# Create a conda environment with Python 3.9.19
conda create --name AWSenv python=3.9.19 -y

# Activate the new environment
conda activate AWSenv

# Install the packages from requirements.txt using pip
pip install -r requirements.txt

# Check Python version
python --version

# List the installed packages
pip freeze
