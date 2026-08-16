import pandas as pd
data = {
    "Name": ['sohail','mohan','rohan','sohan','lohan'],
    "Marks":[77,55,44,33,99],
    "Age":[22,22,33,11,22]
}
df = pd.DataFrame(data)
print(df.head(2))
print(df.tail(4))
print(df.shape)
print(df.columns)
print(df.info)