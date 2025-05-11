# Mock Pandas Coding Test - Quant Developer Interview

import pandas as pd
import numpy as np

# **1. Stock Price Data Manipulation**
# Load a DataFrame with columns ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']
# (a) Compute daily returns.
# (b) Compute the 20-day moving average of the closing price.
# (c) Compute the 30-day rolling volatility of returns.

def process_stock_data(df):
    df['Return'] = df['Close'].pct_change()
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    df['Volatility_30'] = df['Return'].rolling(window=30).std()
    return df

# **2. Handling Missing Data**
# Given a DataFrame with missing stock prices, fill missing values appropriately.

def handle_missing_data(df):
    df['Close'] = df['Close'].ffill().bfill()
    return df

# **3. Resampling Stock Data**
# Convert minute-by-minute price data into daily OHLC format.

def resample_intraday_data(df):
    return df.resample('D').ohlc()

# **4. Portfolio Returns**
# Given a DataFrame of daily returns for multiple stocks, compute portfolio returns and Sharpe ratio.

def compute_portfolio_metrics(returns_df, weights, risk_free_rate=0.0001):
    portfolio_returns = returns_df.dot(weights)
    sharpe_ratio = (portfolio_returns.mean() - risk_free_rate) / portfolio_returns.std()
    return portfolio_returns, sharpe_ratio

# **5. Order Book Processing**
# Compute the mid-price and bid-ask spread from a DataFrame containing order book data.

def compute_market_metrics(order_book):
    best_bid = order_book[order_book['side'] == 'buy']['price'].max()
    best_ask = order_book[order_book['side'] == 'sell']['price'].min()
    mid_price = (best_bid + best_ask) / 2
    spread = best_ask - best_bid
    return mid_price, spread

# **6. Options Pricing (Black-Scholes Model)**
# Implement a function to compute option price given parameters.
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)



# Mock Pandas Coding Test - Quant Developer Interview (Commodity Trading Focus)

import pandas as pd
import numpy as np

# **1. Futures Price Roll Calculation**
# Given a DataFrame with columns ['Date', 'Contract', 'Close', 'Volume', 'Open Interest']
# (a) Identify the most active contract (highest open interest) for each day.
# (b) Construct a continuous futures price series, rolling to the next active contract on expiry.

def roll_futures_contract(df):
    df['Most_Active'] = df.groupby('Date')['Open Interest'].idxmax()
    df_continuous = df.loc[df['Most_Active']]
    return df_continuous[['Date', 'Contract', 'Close']]

# **2. Basis Calculation (Spot vs. Futures Spread)**
# Compute the basis as the difference between spot and nearest futures contract price.

def compute_basis(spot_df, futures_df):
    merged = spot_df.merge(futures_df, on='Date', suffixes=('_spot', '_futures'))
    merged['Basis'] = merged['Close_spot'] - merged['Close_futures']
    return merged[['Date', 'Basis']]

# **3. Seasonal Price Patterns**
# Analyze the seasonal trend of commodity prices.

def compute_seasonal_pattern(df):
    df['Month'] = df['Date'].dt.month
    seasonal_trend = df.groupby('Month')['Close'].mean()
    return seasonal_trend

# **4. Volatility & Spread Analysis**
# Compute the spread between two commodities and rolling volatility.

def compute_spread_volatility(df1, df2):
    merged = df1.merge(df2, on='Date', suffixes=('_c1', '_c2'))
    merged['Spread'] = merged['Close_c1'] - merged['Close_c2']
    merged['Volatility_30'] = merged['Spread'].rolling(window=30).std()
    return merged[['Date', 'Spread', 'Volatility_30']]

# **5. Commodity Storage Arbitrage**
# Compute cost of carry and identify profitable storage opportunities.

def compute_storage_arbitrage(spot_df, futures_df, storage_cost_per_day):
    merged = spot_df.merge(futures_df, on='Date', suffixes=('_spot', '_futures'))
    merged['Cost_of_Carry'] = (merged['Close_futures'] - merged['Close_spot']) - storage_cost_per_day * (futures_df['Contract_Expiry'] - spot_df['Date']).dt.days
    return merged[['Date', 'Cost_of_Carry']]

# **6. Hedging Strategy Analysis**
# Compute daily P&L for a hedged position.

def compute_hedging_pnl(spot_df, futures_df, position_size):
    merged = spot_df.merge(futures_df, on='Date', suffixes=('_spot', '_futures'))
    merged['Hedge_PnL'] = position_size * (merged['Close_futures'].diff() - merged['Close_spot'].diff())
    return merged[['Date', 'Hedge_PnL']]
