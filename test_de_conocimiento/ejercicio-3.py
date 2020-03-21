#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:41:36 2020

@author: andres


3) Unas fichas de dominó se colocan una al lado de otra tal que si una ficha se 
cae empuja a la siguiente. El estado inicial de un arreglo de dominó se muestra 
como una tira de letras, 3 valores posibles:

    D  La ficha se cayó hacia la derecha
    I  La ficha se cayó hacia la izquierda
    -  La ficha está parada
    
Por ejemplo, la tira inicialmente representada como D - - - - - - termina como 
D D D D D D D, significando que todas las fichas fueron volteadas a la derecha.  
Si una ficha es empujada simultáneamente desde ambos lados, esta queda parada 
(o sea, "-").
- - I D - -  termina  I I I D D D
D - - - I I -  termina  D D - I I I -

Construir el algoritmo que dada la condición inicial determine la posición 
final de las fichas.

"""

arr = [ "D", "-", "-", "-", "I", "I", "-" ]

"""
Descripción:

Inserto al princio y al final del array el caracter "-", para poder analizar 
los elementos que están inicialmente en los extremos de la lista, pero al final 
los va a quitar para hallar el resultado final.
El bucle for repite el bicle anidado while hasta que se corta el flujo cuando 
en el bucle while no hubo ningún cambio.
Se agregará el caracter "I" si la posición que se itera es "I", mayor a 1 y su 
1° consecutivo menor es una ficha parada "-" y su 2° ficha menor no cayó a la 
derecha.
Se agregará el caracter "D" si la posición que se itera es "D", menor a la 
anteúltimo elemento de la lista y su 1° consecutivo es mayor es una ficha 
parada "-" y su 2° consecutivo mayor no se cayó a la izquierda. 
"""

arr.append("-")
arr.insert(0, "-")
last = len(arr) - 1

for nro in range(last):
    
    i = 0
    change = False
    
    while i<last:    
                
        if i > 1 and arr[i] == "I" and arr[i-1] == "-" and arr[i-2] != "D":
            arr[i-1]="I"
            change = True    
            
        if i < last - 1 and arr[i] == "D" and arr[i+1] == "-" and arr[i+2] != "I":
            arr[i+1] = "D"
            change = True
            i += 1  # es por el sentido del recorrido ---> hacia la D
        
        i += 1
    
    if change == False:
        break
        

arr.pop()
arr.remove("-")
print("Solución:", arr)