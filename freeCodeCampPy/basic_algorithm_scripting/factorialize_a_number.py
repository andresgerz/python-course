#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:28:34 2020

@author: andres

Return the factorial of the provided integer.
If the integer is represented with the letter n, a factorial is the product of 
all positive integers less than or equal to n.
Factorials are often represented with the shorthand notation n!

For example: 5! = 1 * 2 * 3 * 4 * 5 = 120

Only integers greater than or equal to zero will be supplied to the function.
Remember to use Read-Search-Ask if you get stuck. Write your own code.
"""

def factorialize(nro):
    
    if (nro == 0 or nro == 1):
        return 1
    else: 
        return nro * factorialize(nro-1)
    
nro = int(input("Introduce a value: "))

print(factorialize(nro))