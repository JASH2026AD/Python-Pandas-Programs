import pandas as pd

data = {
    "Name": ["arun", "bharath", "charan", "divya"],
    "City": ["vijayawada", "hyderabad", "guntur", "vizag"]
}

df = pd.DataFrame(data)

# Convert names to uppercase
df["Name"] = df["Name"].str.upper()

# Capitalize city names
df["City"] = df["City"].str.title()

print(df)