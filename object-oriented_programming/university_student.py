#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:19:10 2019

@author: andres
"""

"""
Do a program that's contain a class call stundent and It have attributes as his 
name, note, ... .
Define the methodes for inicialize theirs attributes, print and show the attributes 
with the note if aprobe or not. 
"""

class Student():
    
    # Initialize the attributes
    
    def __init__(self):
        self.name = input("Name: ")  
        self.age = input("Age: ")
        self.degree = input("Degree: ")
        self.note = input("Note: ")
        
    def show_info(self):
        print("-----------------------------------")
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Degree: " + self.degree)
        print("Note: " + str(self.note))
    
    def result(self):
        
        if (float(self.note) >= 6):
            print("Result: " + self.name + " approved.")
            print("-----------------------------------")
            
        else:
            print("Result: " + self.name + " don't approved.")
            print("-----------------------------------")

    
student1 = Student()

student1.show_info()
student1.result()