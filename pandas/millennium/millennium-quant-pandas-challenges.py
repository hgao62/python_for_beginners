import pandas as pd
import numpy as np




# Sample financial datasets for challenges
def generate_stock_data():
    """
    Generate a sample stock price and trading volume dataset
    Columns: Date, Ticker, Open, High, Low, Close, Volume, Returns
    """
    np.random.seed(42)
    dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='B')
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
    
    data = []
    for ticker in tickers:
        ticker_data = pd.DataFrame({
            'Date': dates,
            'Ticker': ticker,
            'Open': np.random.normal(100, 20, len(dates)),
            'High': np.random.normal(105, 20, len(dates)),
            'Low': np.random.normal(95, 20, len(dates)),
            'Close': np.random.normal(100, 20, len(dates)),
            'Volume': np.random.randint(1000000, 10000000, len(dates))
        })
        data.append(ticker_data)
    
    return pd.concat(data, ignore_index=True)


def get_max_min1_return_date(df, column):
    columns = ['Date', 'Returns']
    largest_return = df.nlargest(1,column)
    smallest_return = df.nsmallest(1,column)
    return largest_return[columns],smallest_return[columns]

def get_max_min_return_date2(df, column):
    columns = ['Date', 'Returns']
    largest_return = df.loc[df[column].idxmax()]
    smallest_return = df.loc[df[column].idxmin()]
    return largest_return[columns],smallest_return[columns]

def get_monthly_max_min_return(df):
    df['month'] = df['Date'].dt.to_period('M')
    monthly_extreme = df.groupby('month').agg({"Returns":['max', 'min']})
    return monthly_extreme
        
def generate_trades_data():
    """
    Generate a sample trades dataset with transaction details
    Columns: Trade ID, Date, Ticker, Trade Type, Quantity, Price, Commission
    """
    np.random.seed(42)
    dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='B')
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
    
    data = []
    for _ in range(500):
        trade = {
            'Trade ID': f'TRADE_{np.random.randint(10000, 99999)}',
            'Date': np.random.choice(dates),
            'Ticker': np.random.choice(tickers),
            'Trade Type': np.random.choice(['BUY', 'SELL']),
            'Quantity': np.random.randint(10, 1000),
            'Price': np.random.normal(100, 20),
            'Commission': np.random.uniform(5, 50)
        }
        data.append(trade)
    
    return pd.DataFrame(data)


trade = generate_trades_data()

trade_volume_by_ticker = trade.groupby('Ticker')['Quantity'].agg([("Total Volume","sum"),("Avg Side", "mean")])

trade['net_quantity'] = trade.apply(lambda row: row['Quantity'] if row['Trade Type'] =='BUY' else -row['Quantity'],axis=1)
trade_pos = trade.groupby('Ticker')['net_quantity'].sum().reset_index(name="Net Pos")
print(trade_volume_by_ticker)
print(trade_pos)
# Pandas Challenge Questions
class QuantInterviewChallenges:
    def __init__(self):
        self.stock_data = generate_stock_data()
        self.trades_data = generate_trades_data()
    
    def challenge_1_daily_returns(self):
        """
        Challenge 1: Calculate Daily Returns
        Tasks:
        1. Calculate daily returns for each ticker
        2. Identify dates with highest and lowest returns
        3. Calculate annualized volatility (standard deviation of returns * sqrt(252))
        """
        
        df = self.stock_data
        df['Returns'] = df['Close'].pct_change()
        returns_summary = df.groupby('Ticker')['Returns'].agg([('Mean Return', 'mean'), ('Volatility', lambda x:x.std()*np.sqrt(252))])
        returns_summary2 = df.groupby('Ticker').agg({"Returns":["mean", lambda x:x.std()*np.sqrt(252)]})
        returns_summary2.columns = ["Mean Return", "Volatility"]
        # identify dates with highest and lowest returns
        aapl_df = df[df['Ticker'] == 'AAPL']
        largest_return, smallest_return = get_max_min1_return_date(aapl_df,'Returns')
        monthly_extreme = get_monthly_max_min_return(aapl_df)
        print(returns_summary)
        print(largest_return)
        print(smallest_return)
        print(monthly_extreme)
    
    def challenge_2_trade_analysis(self):
        """
        Challenge 2: Trade Performance Analysis
        Tasks:
        1. Calculate total trading volume per ticker
        2. Calculate average trade size
        3. Compute net position (total buy - total sell) for each ticker
        """
        trade = self.trades_data
        trade['net_quantity'] = trade.apply(lambda row: row['Quantity'] if row['Trade Type'] =='BUY' else -row['Quantity'], axis=1)
        net_pos = trade.groupby('Ticker')['net_quantity'].sum().reset_index(name="Net Pos")
        print(net_pos)
        
        # Calculate trade metrics
        trade_summary = self.trades_data.groupby('Ticker').agg({
            'Quantity': ['sum', 'mean'],
            'Trade Type': lambda x: (x == 'BUY').sum() / len(x)
        })
        trade_summary.columns = ['Total Volume', 'Avg Trade Size', 'Buy Ratio']
        
        # Calculate net position
        buy_trades = self.trades_data[self.trades_data['Trade Type'] == 'BUY']
        sell_trades = self.trades_data[self.trades_data['Trade Type'] == 'SELL']
        
        net_position = pd.DataFrame({
            'Total Buys': buy_trades.groupby('Ticker')['Quantity'].sum(),
            'Total Sells': sell_trades.groupby('Ticker')['Quantity'].sum()
        })
        net_position['Net Position'] = net_position['Total Buys'] - net_position['Total Sells']
        
        return net_position
    
    def challenge_3_rolling_window(self):
        """
        Challenge 3: Rolling Window Analysis
        Tasks:
        1. Calculate 20-day moving average of closing prices
        2. Identify crossover points (where price crosses moving average)
        3. Calculate cumulative returns over rolling windows
        """
        stock_data = self.stock_data
        stock_data['20D moving average'] = stock_data.groupby('Ticker')['Close'].transform(lambda x: x.rolling(20).mean())
        stock_data['Crossover'] = np.where(stock_data['Close'] > stock_data['20D moving average'], "Above", "Below" )
        stock_data['Returns'] = stock_data['Close'].pct_change()
        stock_data['Cum Returns'] = (stock_data['Returns'] +1).cumprod()
        
        return stock_data
        
    
    def challenge_4_performance_attribution(self):
        """
        Challenge 4: Performance Attribution
        Tasks:
        1. Calculate daily dollar trading volume
        2. Analyze trading costs (commission)
        3. Compare trade performance across different tickers
        """
        
        trade = self.trades_data
        trade['Dollar Volume'] = trade['Quantity'] * trade['Price']
        trade['Trading Cost'] = trade['Dollar Volume'] * trade['Commission']
        perf_summary = trade.groupby('Ticker').agg({"Dollar Volume":['sum'], "Trading Cost": ["sum","mean"]})
        perf_summary.columns = ['Ticker', "Total Dollar Volume", "Total Commission", "Avg Commission"]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Daily dollar volume
        self.trades_data['Dollar Volume'] = self.trades_data['Quantity'] * self.trades_data['Price']
        
        # Performance summary
        perf_summary = self.trades_data.groupby('Ticker').agg({
            'Dollar Volume': 'sum',
            'Commission': ['sum', 'mean']
        })
        perf_summary.columns = ['Total Dollar Volume', 'Total Commissions', 'Avg Commission']
        
        return perf_summary
    
    def run_all_challenges(self):
        """
        Run and print results of all challenges
        """
        print("Challenge 1: Daily Returns Summary")
        print(self.challenge_1_daily_returns())
        print("\nChallenge 2: Trade Analysis")
        print(self.challenge_2_trade_analysis())
        print("\nChallenge 3: Rolling Window Analysis")
        print(self.challenge_3_rolling_window().head())
        print("\nChallenge 4: Performance Attribution")
        print(self.challenge_4_performance_attribution())



import pandas as pd
import numpy as np

def generate_commodity_data():
    """
    Generate comprehensive commodity trading dataset
    Columns: Date, Commodity, Contract, Price, Volume, Open Interest, Basis, Spread
    """
    np.random.seed(42)
    dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='B')
    commodities = [
        'Crude Oil WTI', 
        'Natural Gas', 
        'Gold', 
        'Copper', 
        'Corn', 
        'Wheat', 
        'Soybeans'
    ]
    contracts = ['Front Month', 'Next Month', 'Quarter Ahead']
    
    data = []
    for commodity in commodities:
        for contract in contracts:
            # Simulate price movements with some correlation to real-world factors
            base_price = {
                'Crude Oil WTI': 70,
                'Natural Gas': 5,
                'Gold': 1800,
                'Copper': 4,
                'Corn': 6,
                'Wheat': 7,
                'Soybeans': 14
            }[commodity]
            
            commodity_data = pd.DataFrame({
                'Date': dates,
                'Commodity': commodity,
                'Contract': contract,
                'Price': np.cumsum(np.random.normal(0, 1, len(dates))) + base_price,
                'Volume': np.random.randint(1000, 100000, len(dates)),
                'Open Interest': np.random.randint(10000, 500000, len(dates))
            })
            
            # Calculate basis (difference between spot and futures price)
            commodity_data['Basis'] = commodity_data['Price'] * np.random.uniform(0.9, 1.1, len(dates))
            
            # Calculate spread between contracts
            commodity_data['Spread'] = commodity_data['Price'] - commodity_data['Price'].shift(1)
            
            data.append(commodity_data)
    
    return pd.concat(data, ignore_index=True)

df = generate_commodity_data()

print('done')
class CommodityTradingChallenges:
    def __init__(self):
        self.commodity_data = generate_commodity_data()
    
    def challenge_1_seasonal_analysis(self):
        """
        Seasonal Commodity Price Analysis
        Tasks:
        1. Calculate average prices by month for each commodity
        2. Identify seasonal price patterns
        3. Compute price volatility by season
        """
        data = self.commodity_data
        data['Month'] = data['Date'].dt.to_period('M')
        # avg_price = data.groupby(['Month','Commodity'])['Price'].mean().reset_index(name="Avg Price")
        seasonal_analysis = data.groupby(['Month','Commodity']).agg({"Price":['mean', lambda x: x.std()]})
        seasonal_analysis.columns = ["Avg Price", "Volatility"]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Add month column
        # self.commodity_data['Month'] = self.commodity_data['Date'].dt.month
        
        # # Seasonal price analysis
        # seasonal_analysis = self.commodity_data.groupby(['Commodity', 'Month'])['Price'].agg([
        #     ('Avg Price', 'mean'),
        #     ('Price Volatility', 'std')
        # ]).reset_index()
        
        return seasonal_analysis
    
    def challenge_2_spread_analysis(self):
        """
        Commodity Spread and Basis Analysis
        Tasks:
        1. Calculate average spreads between different contract months
        2. Analyze basis risk for each commodity
        3. Identify potential arbitrage opportunities
        """
        data = self.commodity_data
        data['Month'] = data['Date'].dt.month
        avg_price = data.groupby('Month')['Spread'].mean().reset_index(name="Avg Price")
        
        
        
        
        
        
        
        # Spread analysis across contracts
        spread_analysis = self.commodity_data.groupby(['Commodity', 'Contract'])['Spread'].agg([
            ('Avg Spread', 'mean'),
            ('Spread Volatility', 'std'),
            ('Max Spread', 'max'),
            ('Min Spread', 'min')
        ]).reset_index()
        
        return spread_analysis
    
    def challenge_3_trading_volume(self):
        """
        Trading Volume and Open Interest Analysis
        Tasks:
        1. Analyze relationship between price and trading volume
        2. Calculate correlation between price changes and volume
        3. Identify high-liquidity periods
        """
        # Volume analysis
        volume_analysis = self.commodity_data.groupby('Commodity').apply(lambda x: pd.Series({"Avg Volume":x['Volume'].mean(), "Volume Price Correlation":x['Volume'].corr(x['Price']), "Max interest":x['Open Interest'].max(), "Min interest":x['Open Interest'].min()})).reset_index()
        return volume_analysis
       
    
    def  challenge_4_contango_backwardation(self):
        """
        Futures Curve Analysis (Contango vs Backwardation)
        Tasks:
        1. Identify contango and backwardation periods
        2. Calculate term structure of futures prices
        3. Analyze price differences between contract months
        """
       
    def run_all_challenges(self):
        """
        Run and print results of all commodity trading challenges
        """
        print("Challenge 1: Seasonal Price Analysis")
        print(self.challenge_1_seasonal_analysis())
        print("\nChallenge 2: Spread and Basis Analysis")
        print(self.challenge_2_spread_analysis())
        print("\nChallenge 3: Trading Volume Analysis")
        print(self.challenge_3_trading_volume())
        print("\nChallenge 4: Futures Curve Analysis")
        print(self.challenge_4_contango_backwardation())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

class FuturesTermStructureAnalysis:
    def __init__(self):
        self.data = self._generate_futures_data()
    
    def _generate_futures_data(self):
        """Generate sample futures data with multiple contract months"""
        np.random.seed(42)
        dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='B')
        
        # Generate contract months (front month to 12 months out)
        contract_months = pd.date_range(start='2023-01-01', end='2024-01-01', freq='M')
        
        data = []
        # Base prices for different commodities
        commodities = {
            'Crude Oil': {'price': 75, 'vol': 2},
            'Natural Gas': {'price': 3.5, 'vol': 0.2},
            'Gold': {'price': 1800, 'vol': 20}
        }
        
        for date in dates:
            for commodity, specs in commodities.items():
                for i, contract_date in enumerate(contract_months):
                    # Add contango/backwardation effect
                    # Contango for Crude Oil and Natural Gas, backwardation for Gold
                    if commodity in ['Crude Oil', 'Natural Gas']:
                        price_adjust = i * 0.005  # Contango
                    else:
                        price_adjust = -i * 0.005  # Backwardation
                    
                    # Calculate days to expiration
                    days_to_expiry = (contract_date - date).days
                    
                    # Generate price with term structure effect
                    base_price = specs['price'] * (1 + price_adjust)
                    random_factor = np.random.normal(0, specs['vol']/100)
                    price = base_price * (1 + random_factor)
                    
                    data.append({
                        'Date': date,
                        'Commodity': commodity,
                        'Contract_Date': contract_date,
                        'Days_To_Expiry': days_to_expiry,
                        'Price': price
                    })
        
        return pd.DataFrame(data)
    
    def calculate_term_structure(self, specific_date=None):
        """
        Calculate and analyze the term structure of futures prices
        
        Parameters:
        specific_date: datetime, optional - analyze term structure for a specific date
        """
        if specific_date is None:
            specific_date = self.data['Date'].max()
        
        # Get data for specific date
        daily_data = self.data[self.data['Date'] == specific_date]
        
        # Calculate term structure metrics
        term_structure = {}
        for commodity in daily_data['Commodity'].unique():
            commodity_data = daily_data[daily_data['Commodity'] == commodity].copy()
            
            # Sort by days to expiry
            commodity_data = commodity_data.sort_values('Days_To_Expiry')
            
            # Calculate forward rates and spreads
            commodity_data['Forward_Rate'] = (
                commodity_data['Price'].pct_change() / 
                commodity_data['Days_To_Expiry'].diff() * 365  # Annualized
            )
            
            # Fit curve to term structure
            days = commodity_data['Days_To_Expiry'].values
            prices = commodity_data['Price'].values
            f = interpolate.interp1d(days, prices, kind='cubic', fill_value='extrapolate')
            
            # Store results
            term_structure[commodity] = {
                'raw_data': commodity_data,
                'curve_fit': f,
                'term_structure_shape': 'Contango' if prices[-1] > prices[0] else 'Backwardation',
                'price_range': prices[-1] - prices[0],
                'annualized_slope': (prices[-1]/prices[0] - 1) * (365/days[-1])
            }
        
        return term_structure
    
    def analyze_contract_spreads(self, specific_date=None):
        """
        Analyze price differences between contract months
        """
        if specific_date is None:
            specific_date = self.data['Date'].max()
        
        daily_data = self.data[self.data['Date'] == specific_date]
        
        spread_analysis = {}
        for commodity in daily_data['Commodity'].unique():
            commodity_data = daily_data[daily_data['Commodity'] == commodity].copy()
            commodity_data = commodity_data.sort_values('Days_To_Expiry')
            
            # Calculate spreads between consecutive contracts
            spreads = []
            prices = commodity_data['Price'].values
            days = commodity_data['Days_To_Expiry'].values
            
            for i in range(len(prices)-1):
                spread = {
                    'Spread_Days': days[i+1] - days[i],
                    'Spread_Amount': prices[i+1] - prices[i],
                    'Spread_Percent': (prices[i+1]/prices[i] - 1) * 100,
                    'Annualized_Spread': ((prices[i+1]/prices[i]) ** (365/(days[i+1]-days[i])) - 1) * 100
                }
                spreads.append(spread)
            
            # Calculate spread metrics
            spread_analysis[commodity] = {
                'spreads': spreads,
                'avg_spread_percent': np.mean([s['Spread_Percent'] for s in spreads]),
                'max_spread_percent': max([s['Spread_Percent'] for s in spreads]),
                'min_spread_percent': min([s['Spread_Percent'] for s in spreads]),
                'avg_annualized_spread': np.mean([s['Annualized_Spread'] for s in spreads])
            }
        
        return spread_analysis
    
    def plot_term_structure(self, specific_date=None):
        """Plot term structure curves for all commodities"""
        if specific_date is None:
            specific_date = self.data['Date'].max()
        
        term_structure = self.calculate_term_structure(specific_date)
        
        plt.figure(figsize=(15, 8))
        for commodity, data in term_structure.items():
            raw_data = data['raw_data']
            plt.scatter(raw_data['Days_To_Expiry'], raw_data['Price'], 
                       label=f'{commodity} (Actual)')
            
            # Plot fitted curve
            x_smooth = np.linspace(raw_data['Days_To_Expiry'].min(), 
                                 raw_data['Days_To_Expiry'].max(), 200)
            plt.plot(x_smooth, data['curve_fit'](x_smooth), 
                    label=f'{commodity} (Fitted)', linestyle='--')
        
        plt.title(f'Futures Term Structure as of {specific_date.date()}')
        plt.xlabel('Days to Expiry')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def analyze_term_structure_dynamics(self):
        """Analyze term structure dynamics over time"""
        # Calculate daily term structure slopes
        dates = self.data['Date'].unique()
        slopes = []
        
        for date in dates:
            term_structure = self.calculate_term_structure(date)
            for commodity, data in term_structure.items():
                slopes.append({
                    'Date': date,
                    'Commodity': commodity,
                    'Slope': data['annualized_slope'],
                    'Shape': data['term_structure_shape']
                })
        
        return pd.DataFrame(slopes)

# Example usage
analysis = FuturesTermStructureAnalysis()

# Calculate and print term structure
term_structure = analysis.calculate_term_structure()
for commodity, data in term_structure.items():
    print(f"\nTerm Structure Analysis for {commodity}:")
    print(f"Shape: {data['term_structure_shape']}")
    print(f"Annualized Slope: {data['annualized_slope']:.2%}")
    print(f"Price Range: {data['price_range']:.2f}")

# Analyze spreads
spread_analysis = analysis.analyze_contract_spreads()
for commodity, data in spread_analysis.items():
    print(f"\nSpread Analysis for {commodity}:")
    print(f"Average Spread: {data['avg_spread_percent']:.2%}")
    print(f"Max Spread: {data['max_spread_percent']:.2%}")
    print(f"Average Annualized Spread: {data['avg_annualized_spread']:.2%}")

# # Plot term structure
# analysis.plot_term_structure()

# # Analyze term structure dynamics
# dynamics = analysis.analyze_term_structure_dynamics()
# print("\nTerm Structure Dynamics Summary:")
# print(dynamics.groupby('Commodity').agg({
#     'Slope': ['mean', 'std'],
#     'Shape': lambda x: x.value_counts().index[0]  # most common shape
# }))

# Example usage
# if __name__ == "__main__":
#     commodity_challenges = CommodityTradingChallenges()
#     commodity_challenges.run_all_challenges()

# # Example usage
if __name__ == "__main__":
    interview_challenges = QuantInterviewChallenges()
    interview_challenges.run_all_challenges()


