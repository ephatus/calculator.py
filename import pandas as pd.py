import pandas as pd

# Create a DataFrame (table-like structure)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)

print(df)

# Access column
print("Names:", df['Name'])

# Filter rows
print("Scores above 90:")
print(df[df['Score'] > 90])

import pandas as pd

# Create a DataFrame with 3 students
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 22, 19],
    "Grade": [65, 45, 80]
}

df = pd.DataFrame(data)

# Add a column "Passed" where grade > 50 = True
df["Passed"] = df["Grade"] > 50

# Filter only students who passed
passed_students = df[df["Passed"] == True]

print("All Students:\n", df)
print("\nStudents Who Passed:\n", passed_students)
