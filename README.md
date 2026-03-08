Repository: financial_time_series_forecasting
Author: Tejaswini Marolia

Overview

This project demonstrates a modular pipeline for predicting stock prices using LSTM (Long Short-Term Memory) networks. It leverages historical stock data to forecast future closing prices. The workflow is organized into separate modules for better readability, maintainability, and reproducibility.

The project includes:

Data loading from Yahoo Finance

Data preprocessing and scaling

LSTM model construction, training, and evaluation

Prediction and visualization of stock price forecasts

Folder Structure
financial_time_series_forecasting/
│
├─ src/
│   ├─ dataloader.py       # Load and preprocess stock data
│   ├─ model.py            # LSTM model architecture and training functions
│   ├─ predict.py          # Functions to generate predictions
│   ├─ visualize.py        # Plot actual vs predicted prices
│   └─ stock_forecast.py   # Main script to run the full workflow
│
├─ plots/
│   ├─ AAPL_stock_prediction.png     
│   └─ stock_prediction.png
│
├─ run_forecast.py         # Entry point for running the project
├─ requirements.txt        # All Python dependencies
└─ README.md               # Project documentation

Features

Fetches historical stock data using yfinance

Scales data for neural network training using MinMaxScaler

Builds an LSTM model with configurable sequence length and epochs

Visualizes predicted vs actual stock prices

Modular design for easy extension and experimentation

Installation

Clone the repository:

git clone https://github.com/M10Tejaswini/financial_time_series_forecasting.git
cd financial_time_series_forecasting

Create a virtual environment and activate it:

python -m venv venv
# Windows PowerShell
.\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Usage

Run the full forecasting pipeline:

python run_forecast.py

This will:

Load stock data (default: Apple, ticker AAPL)

Preprocess the data

Train the LSTM model

Generate predictions

Save and display a plot of predicted vs actual prices

Example Output

Dependencies

numpy

pandas

matplotlib

scikit-learn

tensorflow

yfinance

All dependencies are listed in requirements.txt.

Notes

The project uses LSTM networks, which are ideal for sequential data like stock prices.

Virtual environment files (venv/) should not be pushed to GitHub—use .gitignore.

You can change the ticker symbol in stock_forecast.py to forecast other stocks.

