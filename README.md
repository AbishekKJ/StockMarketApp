# SUPER SIMPLE STOCK MARKET APPLICATION

Global Beverage Corporation Exchange (GBCE) Stock Market Simulation

Project Overview

This project simulates a simple stock market trading system for the Global Beverage Corporation Exchange (GBCE). The system models trades for common and preferred stocks, supports recording trades, calculating dividend yields, price-to-earnings (P/E) ratios, volume-weighted stock prices, and computing the GBCE All Share Index.

The application is built with Python using poetry for dependency management.

## Project Structure

```bash

StockMarketApp
├── stock_market.py
├── config.py
├── stock_market
│   ├── models
│   │   └── common_stock.py
│   │   └── preferred_stock.py
│   │   └── stock.py
│   │   └── trade.py
│   ├── enums.py
│   ├── gbce.py
├── tests
│   ├── test_common_stock.py
│   ├── test_preferred_stock.py
│   ├── test_gbce.py
├── pyproject.toml

```
### Setup Instructions

1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory>
```

2. Install poetry Dependency Manager

If poetry is not installed, follow these steps:

Linux/macOS:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Windows:

Use the official installer available at Poetry Installation Docs.

3. Install Project Dependencies

Run the following command in the project directory:
```bash
poetry install
```

4. Activate the Virtual Environment

To activate the virtual environment created by poetry:
```bash
poetry shell
```
Run the Application
If the application requires execution, provide the command below:

```bash
poetry run python stock_market.py
```

Running Tests

To run all test cases using pytest:
```bash
poetry run pytest
```
Ensure the test cases cover various stock types, trade scenarios, and market operations.

### Project Features

Common and Preferred Stock Models
Calculate dividend yield and P/E ratio.
Record trades and calculate volume-weighted stock prices.
GBCE All Share Index Calculation:
Compute using the geometric mean of volume-weighted stock prices.
Trade Management: Record and analyze stock trade data.

### Important Notes

Ensure the virtual environment is activated before running any commands.
The pyproject.toml file specifies all dependencies and configurations.
Comprehensive unit tests are included to ensure robust functionality.

### Assumptions

The following assumptions are made while implementing the solution

- Decimal is used as a data type for stock price, dividend values, par value, and trade price as Decimal gives high
  precision and used widely over financial calculations
- The stock types used for the problem - CommonStock and Preferred
- Assumed the code should also accept the stock, trade, and other data as input so added config parameter to load pre-loaded sample data or fetch input
- Input is explicitly passed as Decimal assuming the value will be decimal. We need to consider converting to Decimal before calculation for the safe side
