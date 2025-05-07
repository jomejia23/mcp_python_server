# Python with Cucumber (Behave) Test Automation Framework

This repository contains a test automation framework built using Python with Behave (Python's implementation of Cucumber) for BDD-style testing.

## Overview

This framework combines the power of:
- **Python**: A versatile programming language
- **Behave**: Python's implementation of Cucumber for BDD (Behavior Driven Development)
- **Playwright**: Modern web testing and automation framework

## Features

- BDD approach using Gherkin syntax
- Page Object Model design pattern
- Clean and maintainable test structure
- Easy to read test scenarios
- Cross-browser testing capabilities

## Project Structure

```
mcp_python_server/
├── tests/
│   ├── features/         # Contains feature files
│   │   ├── steps/       # Step definitions
│   │   └── environment.py # Behave environment setup
├── pages/               # Page Object Models
└── requirements.txt     # Project dependencies
```

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tests:
   ```bash
   behave tests/features/
   ```

## Writing Tests

Tests are written in Gherkin syntax:

```gherkin
Feature: Login Functionality
    Scenario: Successful Login
        Given I am on the login page
        When I enter valid credentials
        Then I should be logged in successfully
```

## Best Practices

- Keep features focused and concise
- Use descriptive step names
- Follow the Page Object Model pattern
- Maintain clean and reusable step definitions

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.