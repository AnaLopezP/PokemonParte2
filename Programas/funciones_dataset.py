import pandas as pd
from math import *
import matplotlib.pyplot as plt
import funciones
from collections import Counter

df = pd.read_csv('Pokemon.csv', delimiter= "\n", encoding='UTF-8')
print(df)

df.drop('Type 1')
df.drop('Type 2')
df.drop('Sp. Atk')
df.drop('Sp. Def')
df.drop('Speed')
df.drop('Generation')
df.drop('Legendary')

pokemons = funciones.Pokemon
class csv:
    def __init__(self, caracteristica):
        self.caracteristica = caracteristica

    def mediaAritmetica(self):
        n = self.caracteristica.count()
        sumaValores = 0
        for valor in self.caracteristica:
            sumaValores = sumaValores + valor
        media = sumaValores/n
        return media
    
   