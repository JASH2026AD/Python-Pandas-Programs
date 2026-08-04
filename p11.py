import pandas as pd

data = {
    "Name": ["Arun", "Bharath", "Arun", "Divya", "Bharath"],
    "Marks": [80, 90, 80, 85, 90]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove duplicates
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)