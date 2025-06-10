import pandas as pd

# 1. read csv file located in same folder called file.csv and save the data to variable called df
df = pd.read_csv(r"C:\development\repo\python_for_beginners\pandas\file.csv")
# 2. drop rows that don't have email
df = df.dropna(subset=["Email"])

# 3 fill name column that don't have Name with value "Name missing"
df["Name"] = df["Name"].fillna("Name missing")
df

# 4 filter customers who age is between 25 and 40 inclusive


# 5 calculate the category average value,maximum value and minium value

# 6. Convert name column to lower case

# 7 convert date column to proper date type
df["Date"] = pd.to_datetime(df["Date"])
df["Date"].dt.year

# 8 extract year from Date column and assign it to a new column called Year


# 9 drop duplicate rows


# 10
