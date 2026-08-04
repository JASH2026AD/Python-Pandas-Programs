import pandas as pd

students = pd.DataFrame({
    "ID": [101, 102, 103],
    "Name": ["Arun", "Bharath", "Charan"]
})

marks = pd.DataFrame({
    "ID": [101, 102, 103],
    "Marks": [85, 90, 78]
})

# Merge using ID
result = pd.merge(students, marks, on="ID")

print(result)