"""
Un grupo de científicos está analizando una forma de vida inteligente extraterrestre en la reconocida área 52. Han descubierto que, sorprendentemente, estos usan las mismas letras que nosotros (26 letras, excluyendo la ñ) aunque su alfabeto posee un orden distinto. Se nos encomienda la tarea de reordenar un diccionario en español para que los extraterrestres puedan buscar palabras en nuestra lengua más fácilmente. Diseñar un algoritmo que dada un string que representa todas las letras del alfabeto ordenadas según los extraterrestres y una lista de palabras, devuelva una lista de palabras ordenadas (en el orden que entiendan los extraterrestres)

Ejemplo:
 lista = ['miel', 'extraterrestre', 'al', 'automovil', 'auto', 'revestir']
 alfabeto = 'zyxwvutsrqponmlkjihgfedcba'

def ordenar_extraterrestre(desordenadas, orden_alfabeto):
    # ordenada = ['revestir', 'miel', 'extraterrestre', 'auto', 'automovil', 'al']
    return ordenada
"""

import operator 


lista = ['miel', 'extraterrestre', 'al', 'automovil', 'auto', 'revestir']
alfabeto = 'zyxwvutsrqponmlkjihgfedcba'
 
def ordenar_random(desordenado, orden_alfabeto):
    z = 0
    w = 0
    accu = "0."
    dic = dict() 
    
    # hallo por cada letra de cada palabra los valores de indexación que tiene
    # cada letra del alfabeto random y los voy concatenando y guardando como valores
    # en un diccionario, junto con sus claves que son las palabras.
    for z in desordenado:
        while(w < len(z)):
            accu += str(orden_alfabeto.index(z[w])+10)  # change this sumo 10 por la indexacion de las primero 10 letras da de 0 hasta 9 y no 00 y 09
            w += 1
            
        dic[z] = float(accu)
        accu = "0."
        w = 0
    
    # ordeno el diccionario según sus valores
    dic = sorted(dic.items(), key=operator.itemgetter(1))
    lista2 = list()
    i=0
    
    # agrego las claves del diccionario a una lista
    for i in range(len(desordenado)):
        lista2.append(dic[i][0])

    return lista2

print(ordenar_random(lista,alfabeto))
