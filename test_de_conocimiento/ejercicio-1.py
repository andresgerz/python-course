#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:41:32 2020

@author: andres


1) Existe un tablero (tipo de ajedrez) y una ficha que se puede mover de a un 
paso a cualquiera de los 8 casilleros adyacentes (izquierda, arriba, diagonal, 
etc.) A cada casillero del tablero le corresponde una coordenada, en pares 
ordenados de números, donde(0, 0) es el primero. 

Tenés que programar la solución que, dada una lista de coordenadas, indique el 
número mínimo de pasos que debe realizar la ficha para visitar cada coordenada, 
en el orden dado. La ficha comienza en la primer coordenada de la lista.

Un input de ejemplo podría ser:

[ (0, 0), (1, 2), (1, 3) ]

Y la solución en este caso es 3.

| |X|
+-+-+-+-
| |X| | 
+-+-+-+-
| | | | 
+-+-+-+-+
|I| | | |
+-+-+-+-+-+-+

Una ilustración de este caso: I es donde arranca, va en diagonal hacia arriba a 
la derecha, luego dos veces hacia arriba. Con esos 3 pasos visita las 3 
coordenadas.

"""

arr = [ (0, 0), (0, 0), (1, 3)]


# Posición inicial
xi, yi = (0, 0)
count = 0

"""
Descripción:

El bucle itera el array de tuplas, pero que a su vez tiene un bucle while 
anidado que se activa cuando las coordenada/s de las tuplas es/son mayor/es a la
posición inicial (0, 0), primeramente en este ejemplo avanzará diagonalmente 
incrementando en 1 las coordenadas x e y, luego avanzará verticalmente 
incrementando en 2 a y. En cada incremento la variable count irá contando los 
incrementos para obtener finalmente la solución. 
"""

for x, y in arr:
        
    while xi < x or yi < y:

        if xi < x and yi < y:
            count += 1
            xi += 1
            yi += 1
            
        elif xi < x and yi == y:
            count += 1
            xi += 1
                
        elif xi == x and yi < y:
            count += 1
            yi += 1

print("Solución: ", count)