import pandas as pd

# Example data
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Group by 'Category' and calculate the mean of 'Value' for each group
group_mean = df.groupby('Category')['Value'].mean().reset_index(name="frequency")
group_max = df.groupby('Category')['Value'].max().reset_index(name="Max value")
print(group_mean)



import pandas as pd

# Sample data
data = {
    'Store': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Sales': [100, 150, 200, 250, 300, 350],
    'Quantity': [1, 2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)

# Group by 'Store' and aggregate using dictionary syntax
grouped = df.groupby('Store').agg({
    'Sales': 'sum',       # Total Sales
    'Quantity': 'sum',    # Total Quantity
})

# Display the aggregated DataFrame
print("\nAggregated DataFrame:")
print(grouped)
