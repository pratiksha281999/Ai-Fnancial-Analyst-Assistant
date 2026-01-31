import yfinance as yf
import pandas as pd


def get_stock_data(symbol, period="6mo"):
    """
    Fetch historical stock data from Yahoo Finance
    """
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)

    if data.empty:
        raise ValueError("No data found for the given stock symbol")

    return data
