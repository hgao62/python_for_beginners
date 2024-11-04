import pandas as pd
import numpy as np

# Sample data with NaN values
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, np.nan, 30, 40, np.nan, 60],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02', '2023-01-01', np.nan],
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva', 'Frank'],
    'Age': [25, 30, np.nan, 40, 45, 50],
    'Email': [
        'alice@example.com', 'bob@example.com', 'charlie@example.com', 
        np.nan, 'eva@example.com', 'frank@example.com'
    ]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Converting the Date column to datetime type, where possible
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display the DataFrame
print(df)
df.to_csv("file.csv")