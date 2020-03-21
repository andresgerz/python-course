#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:41:36 2020

@author: andres


2) Dada una tira de números que representa las alturas del perfil de un terreno, 
calcular el agua que queda atrapada entre las cimas en caso de lluvia.

Por ejemplo, el arreglo [ 5, 3, 1, 1, 3, 1 ] se corresponde con las alturas del 
perfil:

#
#
# # x x #
# # x x #
# # # # # #
-----------
5 3 1 1 3 1

Donde x indica agua acumulada. La primer columna es altura 5, segunda 3, etc. 
Notar que no cabe más agua pues se incurriría por el margen derecho. En este 
caso la solución es 4.

"""

""" arr = [ 5, 3, 1, 1, 3, 1 ] """
arr = [ 6, 3, 1, 1, 3, 1, 6, 1, 6, 6 ]

"""
Descripción:
    
Supongo que las alturas del perfil del terreno son números naturales sin 
incluir el cero. Hallo los máximos absolutos y relativos. 
Por último sumo todos los resultados.
"""
# =============================================================================
# 
# arr.append(arr[len(arr) - 1])
# arr.insert(0, arr[0])
# 
# last = len(arr) - 1
# 
# maxrel_index = []
# maxrel_nro = []
# 
# =============================================================================
################## Hallo los máximos relativos y abs, valores e indices

max_nro = max(arr)
counter = 0
for i in arr:
  if (i == max_nro):
    counter += 1

print(max_nro, counter)

""" for nro in range(1, last):
    
    if arr[nro - 1] < arr[nro] and arr[nro] > arr[nro + 1]:
        maxrel_index.append(nro)
        maxrel_nro.append(arr[nro])
        
    if arr[nro - 1] == arr[nro] and arr[nro] > arr[nro + 1] or arr[nro - 1] < arr[nro] and arr[nro] == arr[nro + 1]:
        
        maxrel_index.append(nro)
        maxrel_nro.append(arr[nro])
   """      

#########################################################
# itero los valores necesario, los resto y hallo el lesultado
""" 
minrel = []
        
result = 0

for k in range(len(maxrel_index) - 1):
    
    if maxrel_nro[k] < maxrel_nro[ k + 1 ]:
        minrel.append(maxrel_nro[k])
    
    else:
        minrel.append(maxrel_nro[ k + 1 ])
    
    for l in range(maxrel_index[k] + 1, maxrel_index[ k + 1 ]): 
        
        if arr[l] > minrel[k]:
            arr[l] = minrel[k]
            
        result += minrel[k] - arr[l]

print("Solución: ", result) """