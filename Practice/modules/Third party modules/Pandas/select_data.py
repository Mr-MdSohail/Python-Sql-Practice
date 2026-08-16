import pandas as pd

student = {
    "Name": ["Sohail", "Ali", "Sara", "John"],
    "Age": [21, 20, 22, 19],
    "Marks": [95, 88, 91, 75]
}

df = pd.DataFrame(student)
print(df["Name"])

print(df.loc[2])

