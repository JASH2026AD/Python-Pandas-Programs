import pandas as pd

data = {
    "Name": ["Arun", "Bharath", "Charan", "Divya"],
    "Marks": [80, None, 65, 90],
    "Age": [20, 21, None, 22]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Replace missing Marks with average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Replace missing Age with average
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nUpdated Data:")
print(df)