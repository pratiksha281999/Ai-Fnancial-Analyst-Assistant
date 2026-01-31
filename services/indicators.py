import pandas as pd


def add_technical_indicators(df):
    """
    Add basic financial indicators to stock data
    """

    df = df.copy()

    # Daily returns
    df["Daily_Return"] = df["Close"].pct_change()

    # Moving averages
    df["MA_20"] = df["Close"].rolling(window=20).mean()
    df["MA_50"] = df["Close"].rolling(window=50).mean()

    # Volatility (rolling standard deviation)
    df["Volatility_20"] = df["Daily_Return"].rolling(window=20).std()

    return df
