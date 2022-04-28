import pandas as pd
import numpy as np
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
        


pkmns_mas_media = []
pkmns_menos_media = []

media_pv = csv.mediaAritmetica(funciones.Pokemon.get_pv())
mediana_pv = csv.mediana(funciones.Pokemon.get_pv())

media_pa = csv.mediaAritmetica(funciones.Pokemon.get_pa())
mediana_pa= csv.mediana(funciones.Pokemon.get_pa())

media_pd = csv.mediaAritmetica(funciones.Pokemon.get_pd())
mediana_pd = csv.mediana(funciones.Pokemon.get_pd())

valor_medio = (media_pa + media_pd + media_pv)/3

for i in funciones.lista_id:
    valor_medio_pokemon = (funciones.Pokemon.get_pa() + funciones.Pokemon.get_pd() + funciones.Pokemon.get_pv())/3

    if valor_medio_pokemon >= valor_medio:
        pkmns_mas_media.append(funciones.Pokemon.get_nombre())
    else:
        pkmns_menos_media.append(funciones.Pokemon.get_nombre())

pokemon_en1 = []
pokemon_en2 = []
pokemon_en1.append(pkmns_mas_media[:len(pkmns_mas_media)])
pokemon_en2.append(pkmns_mas_media[len(pkmns_mas_media):])

pokemon_en1.append(pkmns_menos_media[:len(pkmns_menos_media)])
pokemon_en2.append(pkmns_menos_media[len(pkmns_menos_media):])

np.savetxt("Entrenador 1", pokemon_en1, delimeter = ",", fmt ='% s')
np.savetxt("Entrenador 2", pokemon_en2, delimeter = ",", fmt = '% s')