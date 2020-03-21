#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:53:06 2020

@author: andres

Return the length of the longest word in the provided sentence.

Your response should be a number.

Remember to use Read-Search-Ask if you get stuck. Write your own code.
"""

def findLongestWordLength(string):
    
    words = string.split(" ")
    
    result = max(list(map(len, words)))
    
    print(result)
    

findLongestWordLength("The quick brown fox jumped over the lazy dog");