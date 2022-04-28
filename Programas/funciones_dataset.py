import pandas as pd

df = pd.read_csv('Pokemon.csv', delimiter= "\n", encoding='UTF-8')
print(df)

df.drop('Type 1')
print(df)

df.drop('Type 2')
df.drop('Sp. Atk')
df.drop('Sp. Def')
df.drop('Speed')
df.drop('Generation')
df.drop('Legendary')