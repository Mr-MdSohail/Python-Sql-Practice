import pandas as pd
data = {
    "names" : ['sohail', 'mohan','roahn'],
    "marks" : [83,99,20],
    "age" : [22,33,44]
}
df = pd.DataFrame(data)
print(df)