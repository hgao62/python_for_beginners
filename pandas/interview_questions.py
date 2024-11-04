
import pandas as pd
#1. read csv file located in same folder called file.csv and save the data to variable called df
path = r"C:\development\repo\python_for_beginners\pandas\file.csv"
df = pd.read_csv(path)
#2. drop rows that don't have email
cleaned_df = df.dropna(subset=['Email'])

#3 fill name column that don't have Name with value "Name missing"
cleaned_df["Name"] = cleaned_df["Name"].fillna("Name missing")
#4 filter customers who age is between 25 and 40 inclusive
cleaned_df = cleaned_df[(cleaned_df["Age"] >= 25) & (cleaned_df["Age"] <= 40)]

#5 calculate the category average value,maximum value and minium value
avg = df.groupby("Category")["Value"].mean()
max = df.groupby("Category")["Value"].max()
min = df.groupby("Category")["Value"].min()

avg2 = df.groupby("Category")["Value"].mean().reset_index(name="Category Average")

#6. Convert name column to lower case
cleaned_df['Name'] = cleaned_df['Name'].str.lower()

#7 convert date column to proper date type
cleaned_df['Date'] = pd.to_datetime(cleaned_df['Date'])

#8 ex
# tract year from Date column and assign it to a new column called Year
cleaned_df['Year'] = cleaned_df["Date"].dt.year
#9 drop duplicate rows
df_unique = df.drop_duplicates()

#10


import pandas as pd

# Sample data
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Counter party name': ['Investor A', 'Investor B', 'Investor C', 'Investor D'],
    'Ticker symbol': ['AAPL', 'GOOGL', 'MSFT', 'AAPL'],
    'Buy/Sell': ['BUY', 'SELL', 'BUY', 'SELL'],
    'Number of shares': [100, 150, 200, 50],
    'Trade price': [150.0, 2800.0, 300.0, 155.0]
}

# Create the DataFramef
df = pd.DataFrame(data)

#
# AAPl: 50
# GOOG: -150
# ms
# def net_stock_postions(df):
#     def difference(df):
#         return df[df["Buy/Sell"] == "BUY"] - df[df["Buy/Sell"] == "SELL"] 
    
#     df = df.groupby("Ticker symbol")[['Buy/Sell', 'Number of shares']].apply(difference)
    

# Apply the code to create the 'share_with_side' column



def calculate_net_position(df):
    # df['share_with_side'] = df.apply(lambda row: row['Number of shares'] if row['Buy/Sell'] == 'BUY' else -row['Number of shares'], axis=1)
    # net_positions = df.groupby('Ticker symbol')['share_with_side'].sum().reset_index(name='net_position')
    
    def difference(row):
        if row['Buy/Sell'] == 'BUY':
            return row['Number of shares'] 
        else:
            return -row['Number of shares']
    df['Number of shares with side'] = df.apply(difference,axis=1)
    net_position= df.groupby("Ticker symbol")["Number of shares with side"].sum().reset_index(name='Net position')
    return net_position


print(calculate_net_position(df))