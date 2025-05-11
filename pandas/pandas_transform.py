# Transform the 'Value' column to show the mean of each group
import pandas as pd

# Example data
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
df['Rolling_Mean'] = df.groupby('Category')['Value'].apply(lambda x: x.rolling(window=2).mean())
print(df)