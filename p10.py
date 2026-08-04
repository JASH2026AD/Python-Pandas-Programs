import pandas as pd

data = {
    "Name": ["Arun", "Bharath", "Charan", "Divya", "Eswar"],
    "City": ["Vijayawada", "Hyderabad", "Vijayawada", "Guntur", "Hyderabad"],
    "Marks": [78, 92, 65, 88, 74]
}

df = pd.DataFrame(data)

# Average marks by city
print(df.groupby("City")["Marks"].mean())

# Number of students in each city
print(df["City"].value_counts())

# Highest scorer from each city
print(df.groupby("City")["Marks"].max())