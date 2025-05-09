# Playwright Python Test Framework

A BDD test automation framework for testing the Sauce Demo website using Playwright with Python and Behave.

## Technology Stack
- Python
- Playwright
- Behave (Cucumber BDD)
- Page Object Model (POM)

## Project Structure
```
Playwright-python-framework/
├── requirements.txt       # Project dependencies
├── pages/                # Page Objects
│   ├── __init__.py
│   ├── base_page.py      # Base page with common functionality
│   ├── login_page.py     # Login page specific elements and actions
│   └── inventory_page.py # Inventory page specific elements and actions
└── features/            # Behavior tests
    ├── login.feature    # Login scenarios in Gherkin syntax
    ├── environment/     # Test setup and teardown
    │   └── environment.py
    └── steps/          # Step definitions
        └── login_steps.py
```

## Setup Instructions and more details can be found in the documentation.