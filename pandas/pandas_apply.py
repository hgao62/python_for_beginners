# Define a custom function to calculate the range (max - min) for each group
import pandas as pd


import pandas as pd

# Sample data
data = {"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]}
df = pd.DataFrame(data)


# Define a simple function
def square(x):
    return x**2


# Apply the function to a Series
df["A_squared"] = df["A"].apply(square)

print(df)


# Define a function that sums the values of a row
def row_sum(row):
    return row["A"] + row["B"]


# Apply the function to each row
df["Sum"] = df.apply(row_sum, axis=1)
print(df)


# Define a function that calculates the mean of each column
def calculate_mean(column):
    return column.mean()


# Apply the function to each column
mean_values = df.apply(calculate_mean)

print(mean_values)


# Apply a lambda function to double the values in column 'A'
df["A_doubled"] = df["A"].apply(lambda x: x * 2)


print(df)


# Define a function that categorizes values
def categorize(x):
    if x < 3:
        return "Low"
    elif x < 5:
        return "Medium"
    else:
        return "High"


# Apply the function to column 'A'
df["Category"] = df["A"].apply(categorize)

print(df)


# Define a function that takes multiple parameters
def custom_func(a, b):
    return a * 2 + b


# Apply the function to each row, passing two columns
df["Custom_Calc"] = df.apply(lambda row: custom_func(row["A"], row["B"]), axis=1)

print(df)


# Example data
data = {"Category": ["A", "A", "B", "B", "C", "C"], "Value": [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)


def range_func(x):
    return x.max() - x.min()


# Apply the custom function
group_range = (
    df.groupby("Category")["Value"].apply(range_func).reset_index(name="Range")
)
print(group_range)
