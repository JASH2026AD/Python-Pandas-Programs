import pandas as pd

data = {
    "Employee": ["Ravi", "Kiran", "Arjun", "Priya", "Neha"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [60000, 45000, 75000, 55000, 50000],
    "Experience": [3, 2, 5, 4, 3]
}

df = pd.DataFrame(data)

# Employees earning more than 50000
print("Salary > 50000:")
print(df[df["Salary"] > 50000])

# Average salary
print("\nAverage Salary:")
print(df["Salary"].mean())

# Highest salary
print("\nHighest Salary Employee:")
print(df.loc[df["Salary"].idxmax()])

# Average salary by department
print("\nDepartment Average Salary:")
print(df.groupby("Department")["Salary"].mean())