import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [50000, 500, 1500, 12000],
    "Quantity": [2, 10, 5, 3]
}

df = pd.DataFrame(data)

# Create Total column
df["Total"] = df["Price"] * df["Quantity"]

print("Product Data:")
print(df)

# Highest total sales
print("\nHighest Sales Product:")
print(df.loc[df["Total"].idxmax()])

# Total revenue
print("\nTotal Revenue:")
print(df["Total"].sum())

# Sort based on total
print("\nSorted by Total:")
print(df.sort_values("Total", ascending=False))