import pandas as pd
data = {
    "Names": ['soahil','namu','ramu'],
    "marks":[99,88,77]
}
df = pd.DataFrame(data)
df.to_csv("practice/modules/Third party modules/Pandas/students.csv")
print(df)
pd.read_csv("practice/modules/Third party modules/Pandas/students.csv")
pd.read_csv