# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 22:18:47 2018

@author: mellisos
"""


#==============================================================================
# #funcion
# def suma(n1,n2)(
#     n=n1+n2
#     return(n)
#     )
# print(suma(5,10))
#     
##==============================================================================

#==============================================================================
# 
# #Listas
# #
# #list1=[1,2,3]
# #list2=[4,5,6,7,8]
# #
# 
# 
#==============================================================================
#Tuplas


# tup=(1,3,81,10,3,13,13,13)
# t=(1,-2,10)
# 
#==============================================================================

# Diccionaries
# 
# dic={"Alemania":"Berlin","Francia":"Paris","Argentina":"Buenos Aires"}
# 
# 
#==============================================================================

# #Conditionals
# print("Nota de la alumno: ")
# 
# note_student=float(input())
# 
# 
# def evaluation(note):
#     valoration="aprovate"
#     
#     if note<6:
#         valoration="desaprovation"
#     return valoration
# 
# print(evaluation(note_student))
# 
# 
#==============================================================================
#Condicionals:
#     
# age=int(input("Age: "))
# 
# if 0<age<100:
#     print("correct")
# else:
#     print("incorrect")
# 
# 
#==============================================================================
#Condicional:

# 
# salary=int(input("Add salary: "))
# 
# print("His salary is: "+str(salary))
# 
# 
# 
#==============================================================================
# BUCLES:
# i=0
# for i in range(1,10):
#     for j in range(1,10):
#         for k in range(1,10):
#             print(i,j,k)
#     
#==============================================================================
#==============================================================================
#==============================================================================
# # # Bucles:
# # 
# # # l=[1,8,16,32,64,128,512,1024,2054,4108]    
# # #     
# # # for i in l:
# # #     print("Numbers:",i)
# # #     
# # # 
#==============================================================================
#==============================================================================
#==============================================================================
#Bucles:
#==============================================================================
# count=0    
# email=False
#     
# myemail=input("Add your E-mail:")
# 
# for i in "myemail":
#     if (i=="@" and "."):
#         email=True
#     
#         count=count+1
# 
# if (email==True and len(count==1)):
#     print("El email es correcto")
# else:
#     print("El email no es correcot")        
#     
#==============================================================================
#==============================================================================
#  #Bucles:   
# 
# for i in range(0,30,3):
#     print(f"The Doors {i}")
#     
#==============================================================================
# #==============================================================================
# # Bucles while:
#     
# i=1
# while(i<=10):
#     i=i+1
#     print(i)                
# print("finished this bucle")    
#     
#==============================================================================
#==============================================================================
# # Bucle while:    
#     
# age=int(input("Add your age: "))
# 
# while (age<0):
#     
#==============================================================================
#Bluches continue:
#This programm eliminate the vocals    
#==============================================================================
# word=input("Introduce a word: ")
# 
# for k in word:
#     if k=="e" or k=="a" or k=="i" or k=="o" or k=="u":
#         continue
#     print("See the letter: "+k)    
#     
#     
#==============================================================================
# #==============================================================================
# # Generators
# #example funtion
# def generator(limit):
#     
#     nro=1
#     mylist=[]
#     
#     while nro<limit:
#         mylist.append(nro*2)
#         nro=nro+1
#     return mylist
# 
# print(generator(30))    
# 
# #example generator:
# def generator(limit):
#     
#     nro=1
#  
#     while nro<limit:
#         yield nro*2
#         nro=nro+1
#     
# pairs=generator(10)    
# 
# print(next(pairs))
# print("Aquí podría ir más código")
# print(next(pairs))
# print("Aquí podría ir más código")
# print(next(pairs))
# 
#==============================================================================
#==============================================================================
# #Generator yield from
# 
# def return_cities(*cities):
#     for elements in cities:
#         #for subelements in elements:
#             yield from elements
# 
# cities=return_cities("Buenos Aires","Berlín","Resistencia",
#                      "Paris")
# 
# print(next(cities))
# print(next(cities))
# print(next(cities))
# 
# 
#==============================================================================
#==============================================================================
# #Exceptions
# 
# def addition(n1,n2):
#     return n1+n2
# 
# def subtrac(n1,n2):
#     return n1-n1
# 
# def multiply(n1,n2):
#     return n1*n2
# 
# def division(n1,n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError:
#         print("Don't division in zero")
#         return "error operetion"
#     
# while True:    
#     try:    
#         v1=(int(input("Add a integer number: ")))
#         v2=(int(input("Add a integer number: ")))
#         
#         break
#     except ValueError:
#         print("The values don't right")
# 
# operation=input("Add a operation to make (addition, subtrac,multiply, division): ")
# 
# if operation=="addition":
#     print(addition(v1,v1))
#     
# elif operation=="subtrac":
#     print(subtrac(v1,v2))
# elif operation=="multiply":
#     print(multiply(v1,v2))
# elif operation=="division":
#     print(division(v1,v2))
# else:
#     print("operation no contemple")
#     
# print("Operation ejecuted. To be continued to programm")    
# 
# 
#==============================================================================
# Exception
#==============================================================================
# 
# def division():
#     try:
#         n1=(float(input("Introduce the first number: ")))
#         n2=(float(input("Introduce the first number: ")))
#         
#         print("The division is: "+ str(n1/n2))
# 
#      except ValueError:
#          print("The value is incorrect")
#          
#      except ZeroDivisionError:
#          print("Don't to division of zero")
#  
#     print("Calculate finish")
#     
# division()
#     
#==============================================================================
# #==============================================================================
# def division():
#     try:
#         n1=(float(input("Introduce the first number: ")))
#         n2=(float(input("Introduce the first number: ")))
#         
#         print("The division is: "+ str(n1/n2))
#     except:
#         print("There is a error")
#     
#     print("Calculate finish")
#     
# division()
# 
#==============================================================================
# def division():
# 
#     try:
#         n1=(float(input("Introduce the first number: ")))
#         n2=(float(input("Introduce the first number: ")))
#         
#         print("The division is: "+ str(n1/n2))
#     finally:
#         print("Calculate finish")    
# 
# 
# division()
#     
#==============================================================================
#==============================================================================
# def temperature(t):
#     
#     if t<0:
#         raise TypeError("There isn't temperature oben 0 kelvin")
#     elif t>=0:
#         print("this temperature ex")
#     else:
#         print("This temperature exit")
# 
# temperature(273)
#             
# 
#==============================================================================
# #==============================================================================
# import math
# 
# def calculate_s(nro):
#     if nro<0:
#         raise ValueError("The number don't be negative")
#     else:
#         return math.sqrt(nro)
# 
# v=(int(input("Add a number: ")))
# 
# print(calculate_s(v))
# 
# print("Programm finish")
#         
#==============================================================================
#==============================================================================
# # POO
# 
# class car():
#     lengthchassis=250
#     width=120
#     wheels=4
#     inmotion=False
#     
#     def start(self):
#         self.inmotion=True
# 
#     def state(self):
#         if(self.inmotion):
#             return "The car is in motion"
#         else:
#             return "The car is stop "
# 
# mycar=car()       #instanciar una clase
# 
# print("The length the car is: ",mycar.lengthchassis)
# print("The car has",mycar.wheels,"wheels")
# mycar.start()        
#     
# print(mycar.state())
# 
# print("---------To be continued we creating the secont object-------------")
# 
# 
# mycar2=car()
# print("The length the car is: ",mycar2.lengthchassis)
# print("The car has",mycar2.wheels,"wheels")
# print(mycar2.state())
# 
#==============================================================================
# #==============================================================================
# # POO II
# 
# class car():
#     
#     def __init__(self):   #Initial state
#     
#         self.__lengthchassis=250
#         self.__width=120
#         self.__wheels=4
#         self.__inmotion=False
#         
#     def start(self,we_start):
#         self.__inmotion=we_start
#         
#         if (self.__inmotion):
#             check = self.__check_in()
#         
#         if (self.__inmotion and check):
#             return "The car is in motion"
#         elif (self.__inmotion and check==False):
#             return "some is no good in the check"
#         else:
#             return "The car is stop"
# 
#     def state(self):
#         print("The car has", self.__wheels, "ruedas. Un ancho de", self.__width,
#               "y un largo de", self.__lengthchassis)
#         
#         
#     def __check_in(self):
#         print("making check in")
#         
#         self.nafta = "ok"
#         self.oil   = "ok"
#         self.doors = "closed"
#         
#         if (self.nafta == "ok" and self.oil == "ok" and self.doors == "closed"):
#             return True
#         else:
#             return False
#             
# mycar=car()       #instanciar una clase
# 
# print(mycar.start(True))
#     
# mycar.state()
# 
# print("---------To be continued we creating the secont object-------------")
# 
# 
# mycar2=car()
# 
# print(mycar2.start(False))
# 
# mycar2.state()
# 
#==============================================================================
#==============================================================================
#  # inheritance
#  
# class vehicle():
#     
#     def __init__(self ,mark ,model):
#         
#         self.mark = mark
#         self.model = model
#         self.inmotion = False
#         self.acelerate = False
#         self.stop = False
#         
#     def start(self):
#         self.inmotion = True
#     
#     def acelerate(self):
#         self.acelerate = True
#         
#     def stop(self):
#         self.stop = True
#         
#     def state(self):
#         print("Mark: " ,self.mark ,"\n Model: " ,self.model , "\n In motion: ",
#               self.inmotion, "\n Acelerate: ", self.acelerate , "\n Stop: ",
#               self.stop)
#         
# class truck(vehicle):
#     
#     def load(self, to_load):
#         
#         self.loaded=to_load
#             
#         if (self.loaded):
#             return "the truck loaded"
#         else:
#             return "the truck don't loaded"
#        
#         
#         
#         
#         
# class motorcycle(vehicle):
#     make_willy = ""
#     
#     def willy(self):
#         self.make_willy = "I am making willy \n ==========================="
#         
#     def state(self):
#         print("Mark: " ,self.mark ,"\n Model: " ,self.model , "\n In motion: ",
#               self.inmotion, "\n Acelerate: ", self.acelerate , "\n Stop: ",
#               self.stop , "\n", self.make_willy)
#         
# class electricar(vehicle):
#     
#     def __init__(self, mark, model):
#         
#         super().__init__(mark, model)
#         
#         self.autonimy = 100
#         
#     def charge_energy(self):
#         self.charging = True
#         
# 
# class electric_bike(electricar, vehicle):  #HERENCIA MULTIPLE
#     
#     pass
# 
#     
# mymotorcycle = motorcycle("Harley Davinson", "Model S")
# 
# mymotorcycle.willy()
# 
# mymotorcycle.state()
# 
# 
# 
# mytruck = truck("Volvo","Model heavy")               
# 
# mytruck.start()
# mytruck.state()
# print(mytruck.load(True))
# 
# mybike = electric_bike("Peugeot","Sport A")    
#         
#     
#==============================================================================
# #==============================================================================
# # HERENCIA super()
# 
# class person():
#     
#     def __init__(self, name, age, residence):
#         
#         self.name = name
#         self.age = age
#         self.residence = residence
#         
#     def description(self):
#         
#         print("Name :", self.name, "\nAge :", self.age, "\nResidence :", 
#               self.residence)
#         
# class worker(person):
#     
#     def __init__(self, salary, career, name_worker, age_worker,
#                  residence_worker):
#         
#         super().__init__(name_worker, age_worker, residence_worker)
#         
#         self.salary = salary
#         self.career = career
#     
#     def description(self):
#         super().description()
#         
#         print("Salary: $",self.salary,"\nCareer: ", self.career,"years")
#         
#     
# Otto = person("Otto", 42, "Germany" )
# 
# Otto.description()
# 
# print(isinstance(Otto, worker))
#         
#==============================================================================
#==============================================================================
# # Polimorfismo
# 
# class car():
#     
#     def displacement(self):
#         print("I'm moving using four wheels")
# 
# class motorcycle():
#     
#     def displacement(self):
#         print("I'm moving using two wheels")
#         
# class truck():
#     
#     def displacement(self):
#         print("I'm moving using six wheel")
#         
# def displacement_vehicle(vehicle):
#     vehicle.displacement()
#     
# myvehicle = motorcycle()
# 
# displacement_vehicle(myvehicle)
#     
#==============================================================================
# #==============================================================================
# # Metodo de cadenas
# 
# 
# name = input("Write your name: ").lower()
# 
# print(" The name is: ", name.upper())
# print(" The name is: ", name.lower())
# print("The name is: ", name.capitalize())
# print("Is a digit?",name.isdigit())
# print(name,"has: ",name.count("n"))
# print("This word is: ",name.find("a"))
# print("This word is: ",name.rfind("a"))
# print("This word is there only alphanumeric: ",name.isalnum())
# print("This word is there only letters: ",name.isalpha())
# print(name.split("a"))
# print("This word is: ",name.strip())
# print("This word is: ",name.replace("a","o"))   
# 
#==============================================================================
# Modulos
#==============================================================================
# import os
# 
# os.getcwd("c:/Users/mellisos/Desktop/Programming/Python & R ejercicios/Curso de Python)
# open("maths_functions.py")
# 
#==============================================================================
# #==============================================================================
# from package.module_maths import fibonacci
# from package.module_maths import sumar
# 
# #from maths_functions import * alternative, I can to import all 
# #funcions of this module
# 
# sumar(10,28)
# fibonacci(10)
# 
#==============================================================================
#==============================================================================
# except ModuleNotFoundError:
# print("Problem")
# return "Error"
#==============================================================================
# Extern files: Here I created a file, wrote and closed the file.
    
from io import open

# write mode
#==============================================================================
# 
# text_file = open("filextern.txt","w")
# 
# words="Today is a wonderwall day to study Python \n friday"
# 
# text_file.write(words)
# 
# text_file.close()
# 
# 
#==============================================================================
# read mode

#text_file = open("filextern.txt","r")

#==============================================================================
# text = text_file.read()
# 
# text_file.close()
# 
# print(text)

#==============================================================================
# line_text = text_file.readlines()
# 
# text_file.close()
# 
# print(line_text[1]) 
#==============================================================================
#Open the file in mode extension
#==============================================================================
# 
# text_file = open("filextern.txt","a")
# 
# text_file.write("\n I have to study Python to can backend")
# 
# text_file.close()
# 
#==============================================================================
#==============================================================================
# # mode read and write
# 
# text_file = open("filextern.txt","r+")
# 
# text_file.write("\n I have to study Python to can backend")
# 
# text_file.close()
# 
# 
#==============================================================================
#==============================================================================
# #Serialization 
# 
# import pickle
# 
# list = ["Lenny","Roxanne","Grace"]
# 
# file_binary = open("list","wb")
# 
# pickle.dump("list",file_binary)
# 
# file_binary.close()
# 
# del(file_binary)
# 
#==============================================================================
#I read the binary file
fileb = open("list","rb")

ls = pickle.load(fileb)

print(ls)






