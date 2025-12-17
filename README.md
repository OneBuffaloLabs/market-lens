# Market Lens 📈

> **Quantitative finance dashboard built with Streamlit, Pandas, and Python.**

![CI Status](https://github.com/OneBuffaloLabs/market-lens/actions/workflows/ci.yml/badge.svg)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)

## 📖 About

Market Lens is an interactive financial analytics tool designed to visualize market trends and perform quantitative analysis on live data. It leverages **yfinance** for real-time ingestion and utilizes **Pandas** vectorization to perform high-speed data manipulation without inefficient loops.

This project serves as a reference for building lightweight, data-intensive dashboards in Python, demonstrating clean separation of concerns between the data layer (`data_loader.py`) and the presentation layer (`app.py`).

## 🛠 Tech Stack

- **Runtime:** Python 3.8+
- **Framework:** Streamlit
- **Data Manipulation:** Pandas (Vectorized)
- **Data Source:** yfinance API
- **Visualization:** Plotly (Planned)
- **Linting/Formatting:** Ruff

## 🚀 Getting Started

This project includes a `Makefile` to handle environment setup and execution, abstracting away virtual environment management.

### Prerequisites

- Python 3.8+
- Make (Standard on Linux/Mac, optional on Windows)

### Quick Start (Recommended)

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/OneBuffaloLabs/market-lens.git](https://github.com/OneBuffaloLabs/market-lens.git)
    cd market-lens
    ```

2.  **Install Dependencies**
    This command creates a local virtual environment (`venv`) and installs all required packages.

    ```bash
    make install
    ```

3.  **Run the Application**
    Launches the Streamlit server.

    ```bash
    make run
    ```

### Manual Setup

If you cannot use `make`, you can run the standard Python commands:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

##⚡ Features & UsageThe dashboard provides real-time access to financial markets through an interactive sidebar.

1. **Select Assets:** Use the sidebar to choose multiple tickers (e.g., AAPL, BTC-USD, GOOGL).
2. **Market Data Inspector:** View raw OHLCV (Open, High, Low, Close, Volume) data.
3. **Quantitative Analysis:**

- **Normalized Prices:** Assets are rebased to 100 at the start of the period for direct relative comparison.
- **Daily Returns:** Day-over-day percentage changes calculated via vectorized operations.

##⚙️ Developer Command ReferenceWe use `make` to abstract common development tasks.

| Command        | Description                                            |
| -------------- | ------------------------------------------------------ |
| `make install` | Create virtual environment and install dependencies.   |
| `make run`     | Run the Streamlit application (hot-reloading enabled). |
| `make clean`   | Remove virtual environment and compiled bytecode.      |
| `make lint`    | Run `ruff` to identify code quality issues.            |
| `make format`  | Auto-format code using `ruff` (fixes spacing/imports). |
| `make fix`     | Auto-fix linting errors.                               |

##📂 Project Structure

```text
/
├── app.py # Main application entry point & UI layout
├── data_loader.py # Data ingestion logic & vector transformations
├── requirements.txt # Project dependencies
├── Makefile # Command automation
└── .github/ # CI/CD workflows

```

## 🧪 Quality Control

We enforce code quality standards using **Ruff**.

```bash
# Check for errors
make lint

# Auto-format code
make format

```

---

_Built by [@bana0615](https://www.google.com/search?q=https://github.com/bana0615) as an experimental tool for [One Buffalo Labs](https://github.com/OneBuffaloLabs)._

**License**
[MIT](https://www.google.com/search?q=LICENSE) - Copyright (c) 2025 One Buffalo Labs

```

```
