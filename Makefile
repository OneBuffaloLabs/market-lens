# Define environment variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
STREAMLIT = $(VENV)/bin/streamlit

# .PHONY defines targets that aren't files
.PHONY: all help install run clean

# Default target: prompts the user
all: help

# Help command to display available targets
help:
	@echo "----------------------------------------------------------------------"
	@echo "                     MARKET LENS MAKEFILE"
	@echo "----------------------------------------------------------------------"
	@echo "Make commands:"
	@echo "  make install   - Create venv and install dependencies (requirements.txt)"
	@echo "  make run       - Run the Streamlit application"
	@echo "  make clean     - Remove venv and compiled Python files"
	@echo "----------------------------------------------------------------------"

# Task 1.2: Create virtual environment and install dependencies
install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed successfully."

# Task 1.5: Run the app (using the venv's streamlit binary directly)
run:
	$(STREAMLIT) run app.py --server.port 3000

# Clean up environment
clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	@echo "Cleaned up project environment."