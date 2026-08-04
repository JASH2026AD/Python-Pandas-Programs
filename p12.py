import pandas as pd

data = {
    "Name": ["Arun", "Bharath", "Charan", "Divya"],
    "Marks": [70, 82, 68, 90]
}

df = pd.DataFrame(data)

# Increase marks by 5 where marks are below 75
df.loc[df["Marks"] < 75, "Marks"] += 5

print(df)