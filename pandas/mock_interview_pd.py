import pandas as pd
import numpy as np

# Create sample data
sales_data = pd.DataFrame(
    {
        "date": [
            "2024-01-01",
            "2024-01-01",
            "2024-01-02",
            "2024-01-02",
            "2024-01-03",
            "2024-01-03",
        ],
        "product": ["A", "B", "A", "B", "A", "C"],
        "category": [
            "Electronics",
            "Electronics",
            "Electronics",
            "Electronics",
            "Electronics",
            "Kitchen",
        ],
        "quantity": [10, 20, 15, 25, 30, 20],
        "price": [100, 200, 100, 200, 100, 50],
    }
)
sales_data
# 1. calculate revenue by date and by product
sales_data["total"] = sales_data["quantity"] * sales_data["price"]
revenue_by_date_product = (
    sales_data.groupby(["date", "product"])["total"]
    .sum()
    .reset_index(name="total revenue")
)
revenue_by_date_product.sort_values(
    by=["date", "total revenue"], ascending=[True, False]
)

# 2. find product with revenue above average
revenue_by_product = (
    sales_data.groupby("product")["total"].sum().reset_index(name="total revenue")
)
products_avg = revenue_by_product["total revenue"].mean()
products_above_avg = revenue_by_product.loc[
    revenue_by_product["total revenue"] > products_avg
]


# 3.calculate rolling average sales of daily data
daily_sales = (
    sales_data.groupby("date")["total"].sum().reset_index(name="daily revenue")
)
daily_sales["2 day moving avg"] = daily_sales["daily revenue"].rolling(window=2).mean()

# 4 revenue by product and category

revenue_by_product_category = (
    sales_data.groupby(["product", "category"])["total"]
    .sum()
    .reset_index(name="total revenue")
)
revenue_by_product_category

pivot_table = pd.pivot_table(
    sales_data,
    values="total",
    index="category",
    columns="product",
    aggfunc="sum",
    fill_value=0,
)


# Example data with duplicates
df = pd.DataFrame(
    {
        "date": ["2024-01-01", "2024-01-01", "2024-01-02"],
        "product": ["A", "A", "B"],
        "sales": [100, 200, 150],
    }
)

pivot_table = pd.pivot_table(
    df, index="date", columns="product", values="sales", aggfunc="sum", fill_value=0
)

# pivot() will raise error
# df.pivot(index='date', columns='product', values='sales')  # Error!

# pivot_table() works by aggregating duplicate values
df.pivot_table(
    index="date",
    columns="product",
    values="sales",
    aggfunc="sum",  # or 'mean', 'count', etc.
)
import pandas as pd

# Creating the DataFrame manually
data1 = {
    "ticker": [
        "CL1",
        "CL1",
        "CL1",
        "CL1",
        "CL1",
        "CL12",
        "CL12",
        "CL12",
        "CL12",
        "CL12",
    ],
    "contract": [
        "CLG14",
        "CLH14",
        "CLJ14",
        "CLK14",
        "CLM14",
        "CLV25",
        "CLX25",
        "CLZ25",
        "CLF26",
        "CLG26",
    ],
    "start_date": [
        "2014-01-01",
        "2014-01-22",
        "2014-02-21",
        "2014-03-21",
        "2014-04-23",
        "2024-09-21",
        "2024-10-23",
        "2024-11-21",
        "2024-12-20",
        "2025-01-22",
    ],
    "end_date": [
        "2014-01-21",
        "2014-02-20",
        "2014-03-20",
        "2014-04-22",
        "2014-05-20",
        "2024-10-22",
        "2024-11-20",
        "2024-12-19",
        "2025-01-21",
        "2025-01-28",
    ],
}

schedule = pd.DataFrame(data1)

# Convert dates to datetime format
schedule["start_date"] = pd.to_datetime(schedule["start_date"])
schedule["end_date"] = pd.to_datetime(schedule["end_date"])

data = {
    "date": [
        "2014-01-02",
    ],
    "CLG14": [90.04],
}


df = pd.DataFrame(data)
res = []
for _, row in df.iterrows():
    record = {}
    date = row["date"]
    record["date"] = date
    contract_columns = schedule[
        (schedule["start_date"] <= date) & (schedule["end_date"] >= date)
    ]["contract"].to_list()
    data = row[contract_columns].to_dict()
    record.update(data)
    res.append(record)
result_df = pd.DataFrame(res)
result_df.set_index("date", inplace=True)
columns = [
    "CL1",
    "CL2",
    "CL3",
    "CL4",
    "CL5",
    "CL6",
    "CL7",
    "CL8",
    "CL9",
    "CL10",
    "CL11",
    "CL12",
]
result_df = result_df[columns]
