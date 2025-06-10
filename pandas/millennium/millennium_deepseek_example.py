import pandas as pd
import numpy as np

# 1. Data Cleaning and Preparation
# Sample data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=10),
    "Stock_A": [100, 101, np.nan, 103, 105, 2000, 107, 108, 109, 110],
    "Stock_B": [50, 51, 52, np.nan, 54, 55, 56, 57, 58, 59],
}
df = pd.DataFrame(data)

# Fill missing values and remove outliers
df.fillna(method="ffill", inplace=True)
df = df[(np.abs(df["Stock_A"] - df["Stock_A"].mean()) <= 3 * df["Stock_A"].std())]


# 2: Calculate the daily returns, cumulative returns, and rolling 7-day moving average for a given stock price DataFrame.
# Sample data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=10),
    "Price": [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
}
df = pd.DataFrame(data)


# Calculate daily returns
df["Daily_Return"] = df["Price"].pct_change()

# Calculate cumulative returns
df["Cumulative_Return"] = (1 + df["Daily_Return"]).cumprod()

# Calculate rolling 7-day moving average
df["Rolling_7D_MA"] = df["Price"].rolling(window=7).mean()

# 3. Task: Given a DataFrame of stock prices for multiple stocks, calculate the portfolio value over time assuming equal weights for each stock.
# Sample data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=5),
    "Stock_A": [100, 101, 102, 103, 104],
    "Stock_B": [50, 51, 52, 53, 54],
    "Stock_C": [200, 201, 202, 203, 204],
}
df = pd.DataFrame(data)


# Calculate portfolio value with equal weights
df["Portfolio_Value"] = df[["Stock_A", "Stock_B", "Stock_C"]].mean(axis=1)

# 4.Grouping and Aggregation
# Sample data
data = {
    "Stock": ["AAPL", "GOOG", "AAPL", "GOOG", "MSFT"],
    "Quantity": [10, 5, 15, 7, 20],
    "Price": [150, 2800, 152, 2805, 300],
}
df = pd.DataFrame(data)

# Calculate total traded value per stock
df["Traded_Value"] = df["Quantity"] * df["Price"]
result = df.groupby("Stock")["Traded_Value"].sum()


# 5. Resampling Time Series Data
# Sample data
data = {
    "Datetime": pd.date_range(start="2023-01-01 09:30", periods=100, freq="T"),
    "Price": np.random.rand(100) * 100,
}
df = pd.DataFrame(data)

# Resample to daily OHLC
df.set_index("Datetime", inplace=True)
daily_df = (
    df["Price"]
    .resample("D")
    .agg({"Open": "first", "High": "max", "Low": "min", "Close": "last"})
)


# 6.Handling Multi-Index DataFrames
arrays = [
    ["AAPL", "AAPL", "GOOG", "GOOG"],
    pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-01", "2023-01-02"]),
]
index = pd.MultiIndex.from_arrays(arrays, names=("Stock", "Date"))
df = pd.DataFrame({"Price": [100, 101, 2800, 2805]}, index=index)

# Calculate average price per stock
result = df.groupby("Stock")["Price"].mean()


# 7. Applying Custom Functions
# Sample data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=10),
    "Return": np.random.randn(10) * 0.01,
}
df = pd.DataFrame(data)

# Calculate Sharpe ratio (assuming risk-free rate = 0)
sharpe_ratio = df["Return"].mean() / df["Return"].std() * np.sqrt(252)

# 8 pivot table
# Sample data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=30),
    "Stock": ["AAPL"] * 15 + ["GOOG"] * 15,
    "Price": np.random.rand(30) * 100,
}
df = pd.DataFrame(data)

# Create pivot table
df["Month"] = df["Date"].dt.month
pivot_table = df.pivot_table(
    values="Price", index="Month", columns="Stock", aggfunc="mean"
)

# 9 handling missing data
# Sample data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=10),
    "Price": [100, np.nan, 102, np.nan, 104, 105, np.nan, 107, 108, 109],
}
df = pd.DataFrame(data)

# Interpolate missing values
df["Price"].interpolate(method="linear", inplace=True)


import pandas as pd
import numpy as np


# Example 1: Calculating Price Returns and Volatility
def example_1():
    print("Example 1: Calculating Price Returns and Volatility")
    data = {
        "Date": pd.date_range(start="2023-01-01", periods=100),
        "Crude_Oil_Price": np.random.rand(100) * 100 + 50,
        "Gold_Price": np.random.rand(100) * 2000 + 1500,
    }
    df = pd.DataFrame(data)

    df["Crude_Oil_Return"] = df["Crude_Oil_Price"].pct_change()
    df["Gold_Return"] = df["Gold_Price"].pct_change()
    df["Crude_Oil_Volatility"] = df["Crude_Oil_Return"].rolling(
        window=30
    ).std() * np.sqrt(252)
    df["Gold_Volatility"] = df["Gold_Return"].rolling(window=30).std() * np.sqrt(252)

    df["volatitly"] = df["Return"].rolling(window=20).std() * np.sqrt(252)
    print(df.head())
    print("\n")


# Example 2: Analyzing Seasonality
def example_2():
    print("Example 2: Analyzing Seasonality")
    data = {
        "Date": pd.date_range(start="2020-01-01", periods=36, freq="M"),
        "Natural_Gas_Price": np.random.rand(36) * 10 + 2,
    }
    df = pd.DataFrame(data)
    df["Month"] = df["Date"].dt.month
    monthly_avg = df.groupby("Month")["Natural_Gas_Price"].mean()
    print(monthly_avg)
    print("\n")


# Example 3: Spread Analysis
def example_3():
    print("Example 3: Spread Analysis")
    data = {
        "Date": pd.date_range(start="2023-01-01", periods=100),
        "Brent_Crude": np.random.rand(100) * 100 + 50,
        "WTI_Crude": np.random.rand(100) * 100 + 45,
    }
    df = pd.DataFrame(data)
    df["Spread"] = df["Brent_Crude"] - df["WTI_Crude"]
    threshold = 5
    df["Spread_Exceeds_Threshold"] = df["Spread"] > threshold
    print(df.head())
    print("\n")


# Example 4: Inventory Analysis
def example_4():
    print("Example 4: Inventory Analysis")
    data = {
        "Date": pd.date_range(start="2023-01-01", periods=20, freq="W"),
        "Crude_Oil_Inventory": np.random.randint(100, 500, size=20),
    }
    df = pd.DataFrame(data)
    df["Inventory_Change"] = df["Crude_Oil_Inventory"].diff()
    df["Significant Change"] = abs(df["Inventory_Change"]) > 0.1 * df[
        "Crude_Oil_Inventory"
    ].shift(1)
    print(df.head())
    print("\n")


# Example 5: Rolling Correlation Between Commodities
def example_5():
    print("Example 5: Rolling Correlation Between Commodities")
    data = {
        "Date": pd.date_range(start="2023-01-01", periods=100),
        "Gold_Price": np.random.rand(100) * 2000 + 1500,
        "Silver_Price": np.random.rand(100) * 30 + 20,
    }
    df = pd.DataFrame(data)
    df["Rolling correlation"] = (
        df["Gold_Price"].rolling(window=60).corr(df["Silver_Price"])
    )
    print(df.head())
    print("\n")


# Example 6: Forward Curve Analysis
def example_6():
    print("Example 6: Forward Curve Analysis")
    data = {
        "Maturity": ["2023-03-01", "2023-06-01", "2023-09-01", "2023-12-01"],
        "Futures_Price": [50, 52, 51, 49],
    }
    df = pd.DataFrame(data)
    df["Maturity"] = pd.to_datetime(df["Maturity"])
    df = df.sort_values("Maturity")
    df["Forward_Slope"] = df["Futures_Price"].diff()
    print(df)
    print("\n")


# Example 7: Basis Calculation
def example_7():
    print("Example 7: Basis Calculation")
    data = {
        "Date": pd.date_range(start="2023-01-01", periods=100),
        "Spot_Price": np.random.rand(100) * 100 + 50,
        "Futures_Price": np.random.rand(100) * 100 + 52,
    }
    df = pd.DataFrame(data)
    df["Basis"] = df["Spot_Price"] - df["Futures_Price"]
    print(df.head())
    print("\n")


# Example 8: Rolling Average Price
def example_8():
    print("Example 8: Rolling Average Price")
    data = {
        "Date": pd.date_range(start="2023-01-01", periods=100),
        "Copper_Price": np.random.rand(100) * 10 + 3,
    }
    df = pd.DataFrame(data)
    df["Rolling_7D_Avg"] = df["Copper_Price"].rolling(window=7).mean()
    df["Price_vs_Rolling_Avg"] = df["Copper_Price"] - df["Rolling_7D_Avg"]
    print(df.head())
    print("\n")


# Example 9: Commodity Index Calculation
def example_9():
    print("Example 9: Commodity Index Calculation")
    data = {
        "Date": pd.date_range(start="2023-01-01", periods=100),
        "Crude_Oil": np.random.rand(100) * 100 + 50,
        "Gold": np.random.rand(100) * 2000 + 1500,
        "Natural_Gas": np.random.rand(100) * 10 + 2,
    }
    df = pd.DataFrame(data)
    weights = {"Crude_Oil": 0.4, "Gold": 0.3, "Natural_Gas": 0.3}
    df["Commodity_Index"] = (
        df["Crude_Oil"] * weights["Crude_Oil"]
        + df["Gold"] * weights["Gold"]
        + df["Natural_Gas"] * weights["Natural_Gas"]
    )
    print(df.head())
    print("\n")


# Example 10: Event-Driven Analysis
def example_10():
    print("Example 10: Event-Driven Analysis")
    data = {
        "Date": pd.date_range(start="2023-01-01", periods=100),
        "Wheat_Price": np.random.rand(100) * 10 + 5,
    }
    df = pd.DataFrame(data)
    event_dates = ["2023-02-15", "2023-05-01"]
    event_dates = pd.to_datetime(event_dates)
    for event_date in event_dates:
        pre_event_price = df.loc[
            df["Date"] == event_date - pd.Timedelta(days=5), "Wheat_Price"
        ].values[0]
        post_event_price = df.loc[
            df["Date"] == event_date + pd.Timedelta(days=5), "Wheat_Price"
        ].values[0]
        price_change = post_event_price - pre_event_price
        print(f"Event on {event_date}: Price Change = {price_change}")
    print("\n")


# Run all examples
if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
    example_7()
    example_8()
    example_9()
    example_10()
