import pandas as pd
import numpy as np

# Create sample daily returns data
daily_returns = pd.Series([0.01, -0.02, 0.015, -0.01, 0.02])

# Calculate daily volatility
daily_vol = daily_returns.std()
print(f"Daily Volatility: {daily_vol:.4f}")

# Calculate annualized volatility
annualized_vol = daily_vol * np.sqrt(252)
print(f"Annualized Volatility: {annualized_vol:.4f}")

# Same calculation using lambda function
annualized_vol_lambda = (lambda x: x.std() * np.sqrt(252))(daily_returns)
print(f"Annualized Volatility (lambda): {annualized_vol_lambda:.4f}")