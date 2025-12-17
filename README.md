# Market Lens 📈

A quantitative finance dashboard built with Streamlit and Python. This tool demonstrates data ingestion with `yfinance`, vector manipulation with `pandas`, and interactive visualizations using `plotly`.

## 🚀 Current Status: Phase 2 (Data Ingestion)

The application currently fetches live historical data for selected assets (Stocks & Crypto) and displays the raw pricing data in an interactive table.

## 🛠️ Installation & Setup

**Prerequisites:**

- Python 3.8+
- `make` (optional, for convenience)

### Quick Start (using Makefile)

1. **Install dependencies:**

   ```bash
   make install
   ```

2. **Run the application:**

   ```bash
   make run
   ```

### Manual Setup

If you cannot use `make`, run the following:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run app.py

```

##📂 Project Structure\* `app.py`: Main application entry point and UI layout.

- `data_loader.py`: Handles fetching financial data via the `yfinance` API.
- `requirements.txt`: Project dependencies.
- `Makefile`: Command automation for setup and execution.

_Built by [@bana0615](https://www.google.com/search?q=https://github.com/bana0615) as an experimental tool for [One Buffalo Labs](https://github.com/OneBuffaloLabs)._

**License**
[MIT](https://www.google.com/search?q=LICENSE) - Copyright (c) 2025 One Buffalo Labs
