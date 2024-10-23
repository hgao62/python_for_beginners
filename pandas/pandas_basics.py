import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 60000, 90000, 75000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Get the first few rows
print(df.head())

# Get information about the DataFrame
print(df.info())

# Get basic statistics
print(df.describe())

# Select a single column
print(df['Name'])

# Filter rows where Age is greater than 25
print(df[df['Age'] > 25])

# Add a new column based on existing data
df['Tax'] = df['Salary'] * 0.2
print(df)

# Increase salary by 10%
df['Salary'] *= 1.1
print(df)

# Drop a column
df.drop('Tax', axis=1, inplace=True)
print(df)

# Group by City and calculate the average salary
grouped = df.groupby('City')['Salary'].mean()
print(grouped)

# Save to CSV
df.to_csv('employees.csv', index=False)
