import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    "Ticker": ["AAPL", "AAPL", "GOOG", "GOOG", "AAPL", "GOOG"],
    "Date": [
        "2025-04-22",
        "2025-04-29",
        "2025-04-23",
        "2025-04-30",
        "2025-04-15",
        "2025-04-16",
    ],
    "Price": [150, 155, 2700, 2750, 145, 2650],
}
df = pd.DataFrame(data)

# Convert 'Date' to datetime objects
df["Date"] = pd.to_datetime(df["Date"])

# Sort by 'Ticker' and 'Date'
df = df.sort_values(by=["Ticker", "Date"])

# Calculate percentage change of 'Price' within each 'Ticker' group
df["Price_Change"] = df.groupby("Ticker")["Price"].pct_change()

# Print the result
print(df)
