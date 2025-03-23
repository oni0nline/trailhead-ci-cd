name: Python Selenium Test

on:
  push:
    branches:
      - main  # This will trigger the workflow on pushes to the main branch
  pull_request:
    branches:
      - main  # This will also trigger the workflow on pull requests to the main branch

jobs:
  test:
    runs-on: ubuntu-latest  # Use Ubuntu for the environment

    steps:
      - name: Checkout code
        uses: actions/checkout@v2  # This checks out your repository code

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'  # Use Python 3.8 (or change to the version you need)

      - name: Install dependencies
        run: |
          python -m venv venv  # Create virtual environment
          source venv/bin/activate  # Activate the virtual environment
          pip install -r requirements.txt  # Install dependencies from requirements.txt

      - name: Run Selenium test
        run: |
          source venv/bin/activate  # Activate the virtual environment
          python tests/test_selenium.py  # Run the Selenium test

