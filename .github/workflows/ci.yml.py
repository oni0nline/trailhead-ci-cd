name: Selenium Test Workflow

on:
  push:
    branches:
      - main  # Trigger the workflow when changes are pushed to the main branch

jobs:
  test:
    runs-on: ubuntu-latest  # Use the latest Ubuntu environment

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'  # You can change this version if needed

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install selenium webdriver-manager

      - name: Run Selenium test
        run: |
          python test_selenium.py
