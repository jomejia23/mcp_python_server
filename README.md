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

## Setup Instructions

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

To run all tests:
```bash
behave
```

To run specific feature:
```bash
behave features/login.feature
```

To generate Allure reports:
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

## Framework Features

- Page Object Model (POM) design pattern
- BDD scenarios using Gherkin syntax
- Clean and maintainable test structure
- Reusable page components
- Detailed test reporting with Allure
- Configurable browser options
- Error handling and assertions
- Cross-browser testing support