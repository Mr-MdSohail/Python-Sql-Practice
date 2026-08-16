import pandas as pd

student = {
    "Name": ["Sohail", "Ali", "Sara", "John"],
    "Age": [21, 20, 22, 19],
    "Marks": [95, 88, 91, 75]
}

df = pd.DataFrame(student)

# Print students who satisfy:
# Age < 20
# OR
# Marks > 90
print(df[
    (df["Age"]>20) & (df["Marks"]>90)
    |
    (df["Age"]<20) & (df["Marks"]>90)
])
