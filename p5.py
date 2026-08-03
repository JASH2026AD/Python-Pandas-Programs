import pandas as pd

data = {
    "Name": ["Arun", "Bharath", "Charan", "Divya", "Eswar"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [78, 92, 65, 88, 74]
}

df = pd.DataFrame(data)

# Students with marks greater than 75
print("Students with marks > 75:")
print(df[df["Marks"] > 75])

# Highest scorer
print("\nHighest Scorer:")
print(df.loc[df["Marks"].idxmax()])

# Average marks
print("\nAverage Marks:")
print(df["Marks"].mean())

# Sort by marks
print("\nSorted by Marks:")
print(df.sort_values("Marks", ascending=False))