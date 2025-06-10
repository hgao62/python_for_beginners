import pandas as pd
import numpy as np

# Sample Data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=10, freq="D"),
    "Ticker": ["AAPL"] * 10,
    "Open": np.random.uniform(150, 170, 10),
    "High": np.random.uniform(160, 175, 10),
    "Low": np.random.uniform(145, 165, 10),
    "Close": np.random.uniform(150, 170, 10),
    "Volume": np.random.randint(1000000, 5000000, 10),
}

df = pd.DataFrame(data)

# Daily Return Calculation
df["Return"] = df["Close"].pct_change()

# Moving Averages
df["MA_10"] = df["Close"].rolling(window=10).mean()
df["MA_50"] = df["Close"].rolling(window=50).mean()

# Rolling Volatility (20-day)
df["Volatility_20"] = df["Return"].rolling(window=20).std()

print(df)


# 2.Problem: Given stock data with missing values, fill, interpolate, or drop missing values.

# Introduce some NaN values
df.loc[2:4, "Close"] = np.nan

# Forward fill
df["Close_ffill"] = df["Close"].ffill()

# Backward fill
df["Close_bfill"] = df["Close"].bfill()

# Linear Interpolation
df["Close_interpolated"] = df["Close"].interpolate(method="linear")

# Drop rows with NaN
df_cleaned = df.dropna()

print(df)

# 3. sampling and Grouping
# Problem: Convert intraday stock price data to daily OHLC.
# Creating sample intraday data
date_rng = pd.date_range(start="2023-01-01", periods=60, freq="T")  # 60-minute data
df_intraday = pd.DataFrame(
    {
        "Datetime": date_rng,
        "Ticker": ["AAPL"] * 60,
        "Price": np.random.uniform(150, 170, 60),
        "Volume": np.random.randint(1000, 5000, 60),
    }
)
df_intraday.set_index("Datetime", inplace=True)

# Resample to daily OHLC
df_daily = df_intraday["Price"].resample("D").ohlc()

print(df_daily)


# 4. Problem: Compute portfolio returns and Sharpe Ratio.

# Simulated stock returns
returns = pd.DataFrame(
    {
        "AAPL": np.random.normal(0.001, 0.02, 100),
        "MSFT": np.random.normal(0.0012, 0.018, 100),
        "GOOG": np.random.normal(0.0008, 0.022, 100),
    }
)

weights = np.array([0.4, 0.4, 0.2])  # Portfolio weights
portfolio_returns = returns.dot(weights)

# Sharpe Ratio Calculation
risk_free_rate = 0.0001

(portfolio_returns.mean() - risk_free_rate) / portfolio_returns.std()


sharpe_ratio = (portfolio_returns.mean() - risk_free_rate) / portfolio_returns.std()

print(
    f"Portfolio Return: {portfolio_returns.mean():.4f}, Sharpe Ratio: {sharpe_ratio:.4f}"
)

# 5. order book processing

order_book = pd.DataFrame(
    {
        "timestamp": pd.date_range(start="2023-01-01", periods=5, freq="S"),
        "price": [100.5, 101.0, 100.8, 101.2, 100.7],
        "quantity": [50, 60, 40, 30, 70],
        "side": ["buy", "sell", "buy", "sell", "buy"],
    }
)

# Mid-price calculation
best_bid = order_book[order_book["side"] == "buy"]["price"].max()
best_ask = order_book[order_book["side"] == "sell"]["price"].min()
mid_price = (best_bid + best_ask) / 2

# Bid-ask spread
spread = best_ask - best_bid

print(f"Mid-price: {mid_price}, Spread: {spread}")
