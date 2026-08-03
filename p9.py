import pandas as pd

data = {
    "Name": ["Arun", "Bharath", "Charan", "Divya", "Eswar"],
    "Marks": [95, 82, 76, 64, 45]
}

df = pd.DataFrame(data)

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Apply grade function
df["Grade"] = df["Marks"].apply(grade)

print("Student Grades:")
print(df)

# Count each grade
print("\nGrade Count:")
print(df["Grade"].value_counts())

# Students with A or B
print("\nStudents with A or B:")
print(df[df["Grade"].isin(["A", "B"])])