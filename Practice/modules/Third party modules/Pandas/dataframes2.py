import pandas as pd
data = [2,4,6,8]
df=pd.DataFrame(data)
print(df)
df=pd.DataFrame(data, columns=['Roll Numbers'])
print(df)