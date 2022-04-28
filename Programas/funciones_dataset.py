import pandas as pd

df = pd.read_csv('Pokemon.csv', delimiter= "\n", encoding='UTF-8')
print(df)

df.drop('Type 1')
print(df)
