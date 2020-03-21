#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:41:21 2019

@author: andres
"""

"""
Excercise binary gap: make a function that return a long binary gap

"""

import time, sys 

def binary_gap(number):
    
    start = time.time()
    convert_to_binary = bin(number).split("b").pop()
    
    arr = convert_to_binary.split("1")
    
    arr.pop()
    
    array_len = list(map(len, arr))
    
    max_len = max(array_len) 

    print("Memory", sys.getsizeof(arr))
    print("Time: ", (time.time() - start) * 1000, "ms")
    
    return(convert_to_binary, "-->>" ,max_len)   
        

print(binary_gap(143520))
