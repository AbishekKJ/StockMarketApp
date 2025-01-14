# SUPER SIMPLE STOCK MARKET APPLICATION

Global Beverage Corporation Exchange (GBCE) Stock Market Simulation

Project Overview

This project simulates a simple stock market trading system for the Global Beverage Corporation Exchange (GBCE). The system models trades for common and preferred stocks, supports recording trades, calculating dividend yields, price-to-earnings (P/E) ratios, volume-weighted stock prices, and computing the GBCE All Share Index.

The application is built using Python with a focus on clean, maintainable, and production-ready code, adhering to SOLID principles and using poetry for dependency management.

## Requirements:

1. Your company is building the object-oriented system to run that trading.
2. You have been assigned to build part of the core object model for a limited phase 1
3. For a given stock,
    - Given any price as input, calculate the dividend yield
    - Given any price as input, calculate the P/E Ratio
    - Record a trade, with timestamp, quantity, buy or sell indicator and price
    - Calculate Volume Weighted Stock Price based on trades in past 5 minutes
    - Calculate the GBCE All Share Index using the geometric mean of the Volume Weighted Stock Price for all the stocks

## Project Structure

```bash

StockMarketApp
├── stock_market.py
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

## Model Classes

### Stock

Represents a stock base class with the following properties:

- `symbol`: The stock symbol (e.g., TEA, POP)
- `par_value`: The par value of the stock
- `trades`: The list of trades

### CommonStock

Represents a common stock class implementing base class stock with the following properties:

- `symbol`: The stock symbol (e.g., TEA, POP, ALE, JOE)
- `parValue`: The par value of the stock
- `last_dividend`: The last dividend value

### PreferredStock

Represents a preferred stock class implementing base class stock with the following properties:

- `symbol`: The stock symbol (e.g., GIN)
- `parValue`: The par value of the stock
- `last_dividend`: The last dividend value
- `fixed_dividend`: The fixed dividend value


### Trade

Represents a trade with the following properties:

- `timestamp`: The timestamp of the trade
- `quantity`: The quantity of shares traded
- `trade_type`: The trade action/type (buy or sell)
- `price`: The trade price

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

- Decimal is used as a data type for stock price, dividend values, par value and trade price as Decimal gives high
  precision and used widely over financial calculations
- The stock types used for the problem - CommonStock and Preferred
- Assumed the code should also accept the stock, trade and other data as input so added config parameter to load pre-loaded sample data or fetch input
- Input is explictly passed as Decimal assuming value will be decimal. Need to consider converting to Decimal before calculation for safe side
