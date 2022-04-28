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
    
    def mediana(self):
        caracteristica = self.caracteristica.sort_values()  
        caracteristica = caracteristica.reset_index()
        n = self.caracteristica.count()
        par = False
        if n%2 == 0:
            par =True
        
        if par == True:
            rango = (n / 2)
            print("RANGO = "+str(rango))
            rangoNuevo = rango-1
            valor1 = caracteristica[rangoNuevo]
            valor2 = caracteristica[rangoNuevo+1]
            mediana = valor1 +((valor2-valor1)/2)
        
        else: 
            rango = (n+1)/2
            rangoNuevo = rango - 1
            mediana = caracteristica[rangoNuevo]

        return mediana



print(csv.mediaAritmetica(funciones.Pokemon.get_pv()))
print(csv.mediana(funciones.Pokemon.get_pv()))

print(csv.mediaAritmetica(funciones.Pokemon.get_pa()))
print(csv.mediana(funciones.Pokemon.get_pa()))

print(csv.mediaAritmetica(funciones.Pokemon.get_pd()))
print(csv.mediana(funciones.Pokemon.get_pd()))