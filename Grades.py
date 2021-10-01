import pandas as pd
from pandas_datareader import data as web

##Code to get grades in df1

df = pd.read_csv("https://raw.githubusercontent.com/CoreyWarren/Hackon-Hackathon-May-2021/main/CleansedData.csv")
df1=df.iloc[:,20]     
print(df1)

