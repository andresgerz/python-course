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
    
#==============================================================================
# from io import open
# 
#==============================================================================
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

# fileb = open("list","rb")
# 
# ls = pickle.load(fileb)
# 
# print(ls)
#==============================================================================
# #==============================================================================
# #Serialize an object
# 
# import pickle
# 
# class vehicle():
#  
#   def __init__(self ,mark ,model):
#       
#       self.mark = mark
#       self.model = model
#       self.inmotion = False
#       self.acelerate = False
#       self.stop = False
#       
#   def start(self):
#       self.inmotion = True
#   
#   def acelerate(self):
#       self.acelerate = True
#       
#   def stop(self):
#       self.stop = True
#       
#   def state(self):
#       print("Mark: " ,self.mark ,"\n Model: " ,self.model , "\n In motion: ",
#             self.inmotion, "\n Acelerate: ", self.acelerate , "\n Stop: ",
#             self.stop)
# 
# car1=vehicle("Ford","T")
# 
# car2=vehicle("BMW","S")
# 
# car3=vehicle("Peugeot","504")
# 
# cars=[car1,car2,car3]
# 
# file=open("thecars","wb")
# 
# pickle.dump(cars,file)
# 
# file.close()
# 
# del(file)
# 
# file_opening = open("thecars","rb")
# 
# mycars=pickle.load(file_opening)
# file_opening.close()
# 
# for i in mycars:
#     print(i.state())    
#==============================================================================
#==============================================================================
# #Permanent seving
# 
# import pickle
# 
# class person():
#     
#     def __init__(self ,name ,gender ,age):
#         self.name=name
#         self.gender=gender
#         self.age=age
#         print("Created a new person with the name: ", self.name)
#         
#     def __str__(self):
#         return "{} {} {}".format(self.name, self.gender, self.age)
#     
# class list_persons: 
#     persons=[]
#     
#     def __init__(self):
#         list_of_persons=open("file_extern","ab+")
#         list_of_persons.seek(0)
# 
#         try:                    
#             self.persons=pickle.load(list_of_persons)
#             print("Loaded {} persons of the extern : ".format(len(self.persons)))
#         except:
#             print("The file is empty")
#             
#         finally:
#             list_of_persons.close()
#             del(list_of_persons)
#             
#         
#     def add_persons(self,p):
#         self.persons.append(p)
#         self.save_persons_in_extern_file( )
#         
#     def print_persons(self):
#         for p in self.persons:
#             print(p)
#             
#     def save_persons_in_extern_file(self):
#         list_of_persons=open("file_extern","wb")
#         pickle.dump(self.persons, list_of_persons)
#         list_of_persons.close()
#         del(list_of_persons)
#       
#     def print_extern_file(self):
#         print("The information of the extern file is: ")
#         for p in self.persons:
#             print(p)
#         
# mylist=list_persons()      
# person=person("Phil","male",27)
# mylist.add_persons(person)
# mylist.print_extern_file()
# 
#==============================================================================
# p=person("Jonny","male",30)
# mylist.add_persons(p)
# p=person("Katherin","female",22)
# mylist.add_persons(p)
# 
# mylist.print_persons()
#         
#==============================================================================
# Lambda functions
        
#
# toCube = lambda nro: nro**3
# 
# print(toCube(2))
# 
# value = lambda comission:"¡{}! $".format(comission)
# 
# Otto = 20000
# 
# print(value(Otto))
# 
#
#===============================================================================
# filter() Function
#==============================================================================
# 
# def nroPair(nro):
#     
#     if nro % 2 == 0:
#         return True
#
#==============================================================================
# 
# listNro=[12,50,11,91,100]
# 
# print(list(filter(lambda nroPair: nroPair % 2 == 0, listNro )))
#     
# 
# class worker:
#     
#     def __init__(self, name, position, salary):
#         
#         self.name = name
#         self.position = position
#         self.salary = salary
#         
#     def __str__(self):
#         
#         return "{} that work as {} has a salary of {} $".format(self.name, self.position, self.salary)
#     
#     
# listWorkers=[worker("Stefan", "Director", 100000),
#              worker("John", "Senior", 70000),
#              worker("Sascha", "Semi-Senior", 50000),
#              worker("Thelma", "Junior", 30000)]
# 
# 
# highSalary = filter(lambda employee: employee.salary > 50000, listWorkers)
#     
# for employeeSalary in highSalary:
#     
#     print(employeeSalary)
#         
#

#===================================================================================
# map() function
#==============================================================================
# 
# class worker:
#     
#     def __init__(self, name, position, salary):
#         
#         self.name = name
#         self.position = position
#         self.salary = salary
#         
#     def __str__(self):
#         
#         return "{} that work as {} has a salary of {} $".format(self.name, self.position, self.salary)
#     
#     
# listWorkers=[worker("Stefan", "Director", 100000),
#              worker("John", "Senior", 70000),
#              worker("Sascha", "Semi-Senior", 50000),
#              worker("Thelma", "Junior", 30000)]        
#         
#         
# def calculateComission(worker):
# 
#     if (worker.salary <= 50000):
#         worker.salary = worker.salary*1.03       
#     
#     return worker
# 
# listWorkersComission = map( calculateComission, listWorkers )
# 
# for worker in listWorkersComission:
#     
#     print(worker)
#     

#======================================================================================================
# Regulars expressions
# 
# import re
#==============================================================================

#string = "I go learn regular expression in Python. Python is an easy language."

#print(re.search("learn", string))

#searchText = "Python"


# if re.search(searchText, string) is not None:
#     
#     print("I had find a text")
#     
# else:
#     print("I hadn't find a text")
# 

# textFinded = re.search(searchText, string)
# 
# print(textFinded.start())
# print(textFinded.end())
# print(textFinded.span())
# print(re.findall(searchText, string))
# print(len(re.findall(searchText, string)))
# 

#======================================================================================================
# Regulars expressions


# import re
# 
# list_names = ['Martin Morrison', 
#              'Ellen Anderson',
#              'Arnold Morrison',
#              'Anon Random',
#              'Cosme Fulanito',
#              'Lalo Landa',
#              'Ellen Müller',
#              'Carl Friedrich Gauß',
#              'Carl Friedrich Gauss'
#              ]
# 
# for element in list_names:
#     
#     if re.findall('^Ellen', element):                
#         print(element)
# 
# print("==========================")
# 
# 
# for element2 in list_names:
#     if re.findall('Morrison$', element2):                
#         print(element2)
# print("==========================")        
# 
# 
# for element3 in list_names:
#     
#         if re.findall('[ß]', element3):
#             print(element3)
# print("==========================")        
# 
# 
# for element4 in list_names:
#     
#         if re.findall('Gau[ßs]', element4):
#             print(element4)
# print("==========================")        
# 
# 
# for element5 in list_names:
#     
#         if re.findall('^[A-D]', element5):
#             print(element5)
# print("==========================")    
# print("==========================")    
# print("==========================")    
#     
#             
# list_cars = ['Ford1',
#              'Ford2',
#              'BMW1',
#              'Jagua1',
#              'BMW2',
#              'Maybach1',
#              'BMW3',
#              'Porsche1',
#              'Mercedes Benz1',
#              'BMW4',
#              'Volkswagen1',
#              'Volkswagen2',
#              'BMW5']
# 
# for cars in list_cars:
#     
#     if re.findall('BMW[2-4]', cars):
#         
#         print(cars)
# 
#==============================================================================
# # Regular espression match() and search()
# 
# import re
# 
# name1 = "Karl Marx"
# name2 = "Vladimir Valentinovich Zukov"
# name3 = "marie Houston"
# 
# 
# if re.match("Marie", name3, re.IGNORECASE ):
#     
#     print("I finded the name")
#     
# else:
#     print("I don't finded the name")
#     
# print("==========================")    
# print("==========================")    
# print("==========================")     
#     
#     
# if re.search("Zukov", name2):
#     
#     print("I finded the name")
#     
# else:
#     print("I don't finded the name")
#     
# 
#==============================================================================
# # decorator function
# 
# def function_decorator(functionParameter):
#     
#     def functionInside(*args, **kwargs):
#         
#         print("We go to realice a calculus: ")
#         
#         functionParameter(*args, **kwargs)
#             
#         print("Had finish the calculate: " )        
#         
#     return functionInside
# 
# 
# @function_decorator
# def add(nro1, nro2, nro3):
#     print(nro1 + nro2 + nro3)
# 
# @function_decorator
# def substraction(n1, n2):
#     print(n1-n2)
#    
# @function_decorator    
# def power(base, exponent):
#     
#     print(pow(base, exponent))
#     
# add(15, 20, 100)
# substraction(20, 2)
# power(5, 2)
# 
# power(base=2, exponent=3)
# 
# 
# def comment():
#     
#     """this function make many calculates and
#     It very usefull to work in hard days"""
#     print(40+2)
# 
# 
# print(comment.__doc__)
# comment()
# 
# help(comment)
# 
#==============================================================================
# PYTHON COURSE INTERMEDIE: introduction
#==============================================================================
# 
# class Person():
#     age=18
#     
#     def __init__(self, name, nationality):
#         self.name = name
#         self.nationality = nationality
#         
#     def toSwim(self):
#         print("I'm swimming")
#         
# person1 = Person("Otto","Deutscher")
# print(Person.age)
# print(person1.name)
# print(person1.toSwim())
# 
# 
# class Person2():
#     
#     def __init__(self):
#         pass
#     
#     def sayGoodbye(self):
#         print("Goodbye")
#     
#     @classmethod
#     def greet(cls, name):
#         print("I'm greeting " + name)
#         
# print(Person2.greet("Stella"))
# 
# 
# class Dog():
#     
#     def __init__(self):
#         pass
#     def toEat(self):
#         print("eating")
#     
#     @classmethod
#     def toRun(cls):
#         print("running")
# 
#     @staticmethod
#     def toJump():
#         print("Jumping")
#         
# Snoopy = Dog() 
# Snoopy.toJump()
#
# 
# class Circle:
#     
#     def __init__(self, radius):
#         self.radius = radius
#         
#     @property
#     def area(self):
#         return 3.1416*(self.radius**2)
#         
# c = Circle(10)
# print(c.area)
#==============================================================================
# # Polymorphism
# 
# class cat():
#     def moving(self):
#         print("cat")
#         
# class monkey():
#     def moving(self):
#         print("monkey")
# 
# def toMove(animal):
#     animal.moving()
#     
# cat = cat()
# monkey = monkey()
# cat.moving()
# monkey.moving()
# 
# toMove(cat)
# toMove(monkey)
# 
# 
#==============================================================================
# Introspection


# class Intro():
#     Introver = 9
#     def __init__(self, value):
#         self.value = value
#         
#     def second(self):
#         print("Second")
# 
#     def third(self):
#         print(Third)
#         
# date = Intro("value")
# print(dir(date))
# 
# print(isinstance(date, Intro))
# 
# print(hasattr(date, "Introver"))

# 
#==============================================================================
# Threads
# 
# import threading
# import time 
# 
# class myThread(threading.Thread):
#     
#     def run(self):
#         print("{} starting".format(self.getName()))
#         time.sleep(1)
#         print("{} finished".format(self.getName()))
#         
# if __name__ == "__main__":
#     for x in range(4):
#         hilo = myThread(name="Thread-{}".format(x+1))
#         hilo.start()
#         time.sleep(.1)
#         
#  
#==============================================================================
#

#==============================================================================
# for i in open("dataList.txt"):
#     
#     print(i)
#     
# 
# def numbers():
#     
#     n=2
#     while True:
#         yield n
#         n+=1
# 
# j=numbers()
# print(j)
# print(j.__next__())
# print(j.__next__())        
# 
#==============================================================================
# Decorator


# def firstD(function):
#     def functionDecorator(*args, **kkwars):
#         print("First decorator")
#     return functionDecorator
# 
# 
# @firstD
# def function():
#     print("My first decorator")
#     
# function()
#==============================================================================
# functional programming   
#==============================================================================
# 
# def lettersLower(element):
#     return element.lower()
# 
# listCities = ["Sydney","BOMBay","CABA"]
# print(list(map(lettersLower, listCities)))
# 
# print([cad.lower() for cad in listCities])
# 
#==============================================================================
# 
# def greetings(language):
#     def greeting_es():
#         print("Hola")
#     def greeting_en():
#         print("Hello")
#     def greeting_de():
#         print("Hallo")
#     def greeting_ru():
#         print("Priviet")
#         
#     languages_func={"es": greeting_es,
#               "en": greeting_en,
#               "de": greeting_de,
#               "ru": greeting_ru
#                    }
#     
#     return languages_func[language]
# 
# greeting = greetings("de")
# greeting()
#     
# 
# from functools import reduce
# 
# nros = (1,20,7,11)
# 
# def toAdd(k,l):
#     return k+l
# 
# resultNros = reduce(toAdd, nros)
# print(resultNros)
#  
#==============================================================================
# Regular expression
    
# import re
# 
# print(re.search(r"k", "kilometer"))
# print(re.search(r"\d\d", "kilo42meter"))
#    
# pattern = re.compile("\d\d")
# print(pattern.search( "kilo42meter").group())
# 
# if(re.search("\Aa[0-9].*(end|fin)$","a4 is a step fin")):
#     print("It Found the pattern")
#     
# 
# print(re.sub(r"\d","*","2route660012",4))
#     
#     
# regex = re.compile(r"ac", re.IGNORECASE)    
# print(regex.search("Action"))
# 
#==============================================================================
# Pandas library: data frames
#==============================================================================
# 
# import pandas as pd
# import numpy as np
# 
# dictionary={'Names':
#     ['Steve','Angela','Esther','Jonas'] ,'Grades':
#     ['4','7','10','1'],'Sports':
#     ['swimming','football','running','cycling'],'subjects':
#     ['Physic','Math','Chemical','Logic']} 
# 
# df=pd.DataFrame(dictionary)
# print(df)
# 
# print('\n'*2)
# # Datas not valide
# dictionary2={'Names':
#     ['Steve','Angela','N/A','Jonas'] ,'Grades':
#     ['4','7',np.nan,'1'],'Sports':
#     ['swimming','N/A','running','cycling'],'subjects':
#     ['Physic','N/A','Chemical','Logic']} 
# 
# df2=pd.DataFrame(dictionary2)
# print(df2)
# print('\n'*2)
# print(df2.info())
# print('\n'*4)
# 
# 
# # basic statistics
# print(df2.describe())
# 
# 
# print('\n'*4)
# df3=pd.DataFrame(df2)
# df3=df3.replace(np.nan,"0")
# print(df3)
# 
# 
# print('\n'*4)
# df4=pd.DataFrame(df2)
# df4.dropna(how="any", inplace=True)
# print(df4)
# print('\n'*2)
# 
# 
# # eliminate record searching for column
# column=df2[df2["Names"]!="N/A"]
# print(column)
# print('\n'*4)
# 
# 
# # Convert anywhere nan value to 0
# df3=pd.DataFrame(df2)
# df3.fillna(0, inplace=True)
# print(df3)
# print('\n'*4)
# # Convert to integer numbers
# df3['Grades']=df3.Grades.astype(int)
# print(df3.describe())
# 
# 
# print('\n'*4)
# print("Mean: ",df3['Grades'].mean())
# print("Maximun value: ",df3['Grades'].max())
# 
#==============================================================================
# Pandas library: basics statistics for CSV files
#==============================================================================
# 
# import pandas as pd
# import numpy as np
# 
# atp_data = pd.read_csv('atp-tour-data.csv',encoding = "ISO-8859-1")
# 
# print(atp_data.info())
# print(atp_data.head())
# 
# atp_df = pd.DataFrame(atp_data)
# print(atp_df)
# print('\n'*4)
# 
# atp_df = atp_df.replace(np.nan, "0")
# atp_df = atp_df.replace("N/A", "0")
# atp_df = atp_df.replace("NR", "0")
# 
# # Statistics without NR, N/A and NAN
# print(atp_df.describe(include=[np.number]))
#==============================================================================
# Pandas Library: How select rows and columns in CSV files?
#==============================================================================
# 
# import pandas as pd
# 
# atp_data = pd.read_csv('atp-tour-data.csv',encoding = "ISO-8859-1")
# 
# print(atp_data.info())
# print(atp_data.head())
# print(atp_data.iloc[0:5])
# 
# # Selected rows
# print(atp_data.iloc[[1,3,4,8],])
# 
# # Selected columns
# print(atp_data.iloc[:,0:2])
# 
# # Selected rows and columns
# print(atp_data.iloc[[0,4,5],[1,2]])
#==============================================================================
# Pandas library: selection of rows and columns for names LOC

#==============================================================================
# import pandas as pd
# 
# atp_data = pd.read_csv('atp-tour-data.csv',encoding = "ISO-8859-1") 
# print(atp_data.head())
# 
# atp_data.set_index("Location", inplace=True)
# print("Melbourne")
# print(atp_data.loc["Melbourne"])
# print('\n'*5)
# print("Atlanta and kind of surface:")
# print(atp_data.loc["Atlanta","Surface"])
# 
# print('\n'*5)
# print("Extend selection")
# print(atp_data.loc[["Atlanta","Melbourne"],["Series","Court"]])
# 
# 
# print('\n'*5)
# print("Selection with range")
# print(atp_data.loc[["Atlanta","Melbourne"],"Series":"Round"])
# 
# 
# print('\n'*5)
# print("Selected only grand slam")
# print(atp_data.loc[atp_data["Series"].str.endswith("Slam")])
#==============================================================================
# Pandas library: export to CSV file
#==============================================================================
# 
# import pandas as pd
# 
# data = pd.read_csv('atp-tour-data.csv',encoding = "ISO-8859-1") 
# df = pd.DataFrame(data)
# data.set_index("Location", inplace=True)
# df = data.loc["Melbourne"]
# df.reset_index().to_csv("selected_melbourne.csv", header=True, index=False)
#==============================================================================
# Pandas library: data's search with conditions
#==============================================================================
# 
# import pandas as pd
# 
# data = pd.read_csv('atp-tour-data.csv',encoding = "ISO-8859-1") 
# data.set_index("Location", inplace=True)
# 
# # Many conditions
# print(data.loc[data["Series"].str.endswith("Slam")&(data["Surface"]=="Clay")&(data["Winner"]=="Federer R.")&(data["Round"]=="The Final")])
# 
#==============================================================================
# Pandas library: order values for columns
#==============================================================================
# import pandas as pd
# import numpy as np
# 
# df = pd.read_csv('DatosYT.csv',encoding = "ISO-8859-1") 
# print(df.dtypes)
# 
# df2=pd.DataFrame(np.sort(df.values,axis=0),index=df.index,columns=df.columns)
# print(df2)
#==============================================================================
# # Pandas library: remove rows in a dataframe
# 
# import pandas as pd
# 
# dfsongs = pd.read_csv("canciones.csv")
# print(dfsongs.info())
# print(dfsongs)
# filas=len(dfsongs.index)
# print("Filas:", filas)
# 
# dfsongs.drop(dfsongs.index[[filas-1]], inplace = True)
# filas=len(dfsongs.index)
# print("Filas:", filas)
# print(dfsongs)
# 
#==============================================================================
# Pandas library: write to infomation in a fila CSV
#==============================================================================
# 
# dic = {
#    "Chaco":"Resistencia",
#    "Capital Federal":"CABA",
#    "Córdoba":"Córdoba",
#    "Corrientes":"Corrientes"
#        }
# 
# file = "ciudades.csv"
# csv = open("ciudades.csv","w")
# title="provincia, capital\n"
# csv.write(title)
# 
# for key in dic.keys():
#     provincia = key
#     capital = dic[key]
#     filas = provincia + "," + capital + "\n"
#     csv.write(filas)
#==============================================================================
# NumPy library:    
#==============================================================================
#     
# import numpy as np
# 
# a=np.array([1,2,3,4,5])
# 
# print("Matriz unidimensional:", a)
# 
# a2=np.array([(1,2,3,4,5),(6,7,8,9,10)])
# print("Matriz bidimentional: ",a2)
# 
# 
# import sys
# 
# S=range(1000)
# print("Memory's result of python's list: ", sys.getsizeof(5)*len(S))
# 
# 
# D=np.arange(1000)
# print("Memory's result of NumPy's array: ", D.size*D.itemsize)
# 
# 
# import time
# 
# SIZE = 1000000
# 
# L1 = range(SIZE)
# L2 = range(SIZE)
# A1 = np.arange(SIZE)
# A2 = np.arange(SIZE)
# 
# start = time.time()
# result=[(x,y) for x,y in zip(L1,L2)]
# print("===========================")
# print("Python's list result: ", (time.time() - start)*1000)
# print("===========================")
# print("===========================")
# start = time.time()
# result=A1+A2
# print("Numpy's array result: ", (time.time() - start)*1000)
# 
# 
# nros = np.ones((4,6))
# print(nros)
# 
# nros2 = np.zeros((4,6))
# print(nros2)
# 
# ran = np.random.random((3,3))
# print(ran)
# 
# 
# emp = np.empty((4,4))
# print(emp)
# 
# al = np.full((3,3),2.71)
# print(al)
# 
# sec1 = np.arange(0,36,3)
# print(sec1)
# 
# sec2 = np.linspace(0,1,10)
# print(sec2)
# 
# import pandas as pd
# 
# print(ran.ndim)
# print(ran.dtype)
# print(ran.size)
# print(ran.shape)
# print(ran.max)
# print(ran.min())
# print(ran.sum())
# print(np.sqrt(ran))
# 
#==============================================================================
# Matplotlib library
#==============================================================================
# 
# import matplotlib.pyplot as plt
# 
# a = [2,4,6,8,10]
# c = [10,20,30,40,50]
# 
# plt.plot(a, c, color='blue', linewidth = 3, label = 'línea')
# plt.legend()
# plt.show()
# 
# 
#==============================================================================
# Matplotlib library
#==============================================================================
# 
# import matplotlib.pyplot as plt
# 
# # Define the data
# x1 = [1,5,7,8]
# y1 = [0,5,2,2]
# 
# # Configuration of the graphic's characteristics  
# plt.plot(x1 ,y1 , label = 'line 1', linewidth = 4, color = 'blue')
# 
# # Define the title and the name
# plt.title('Lineal diagram')
# plt.ylabel('Axis y')
# plt.xlabel('Axis x')
# 
# # Show to legend, grid and figure
# plt.legend()
# plt.grid()
# plt.show()
# 
#==============================================================================
# # Scikit Learn library
# 
# import numpy as np
# from sklearn import datasets, linear_model
# import matplotlib.pyplot as plt
# 
# ### Prepare the data 
# 
# # I import the data of the scikit-learn's library
# boston=datasets.load_boston()
# print(boston)
# print()
# 
# ### Understanding of the data
# 
# # I check the information container in dataset
# print("The information in dataset: ")
# print(boston.keys())
# print()
# 
# # I check the characteristic of dataset
# print("The characteristics of dataset:")
# print(boston.DESCR)
# 
# # I check the quantity of data what are there in the datasets
# print("Number of data: ")
# print(boston.data.shape)
# print()
# 
# # I check the information of the columns
# print("Number of columns: ")
# print(boston.feature_names)
# 
# ### Prepare the data of lineal regression simple
# 
# # I selected only the column 5 of dataset 
# X = boston.data[:, np.newaxis,5]
# 
# # I define the data corresponding to the tags
# y = boston.target
# 
# # I graphic the data corresponding
# plt.scatter(X,y)
# plt.xlabel("Number of bedrooms: ")
# plt.ylabel("Average value: ")
# plt.show()
# 
# ### lineal regression single implementation
# from sklearn.model_selection import train_test_split
# 
# # I separate of "train"'s data and test 
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 
# # I define the algorithm to use
# lr = linear_model.LinearRegression()
# 
# # I train the model
# lr.fit(X_train, y_train)
# 
# # I make a prediction
# Y_pred = lr.predict(X_test)
# 
# # I graphic the data together to model
# plt.scatter(X_test, y_test)
# plt.plot(X_test, Y_pred, color="red", linewidth=3)
# plt.title("Lineal regression single")
# plt.xlabel("Number of bedrooms: ")
# plt.ylabel("average value: ")
# plt.show()
# 
# print()
# print("Data of the lineal regression single")
# print()
# print("Pending's value or coefficient a: ")
# print(lr.coef_)
# print("Intersection's value or coefficient b: ")
# print(lr.intercept_)
# print()
# print("The model's ecuation is equal to: ")
# print("y = ", lr.coef_, " x ", lr.intercept_)
# 
# print()
# print("Model's precision: ")
# print(lr.score(X_train, y_train))
# 
#==============================================================================
#==============================================================================
# # Scikit Learn library
# 
# # I import the library what am I going to use
# from sklearn import datasets, linear_model
# 
# ### prepare to the data
# 
# # I import the data from the same library
# boston = datasets.load_boston()
# print(boston)
# print()
# 
# ### data understanding
# 
# # I check the data contain in dataset
# print("Information in dataset: ")
# print(boston.keys())
# print()
# 
# # I check the dataset's characteristics
# print("Dataset's characteristics: ")
# print(boston.DESCR)
# print()
# 
# # I check the number of data in the dataset
# print("Number of data: ")
# print(boston.data.shape)
# print()
# 
# # I check the information of the columns
# print("Columns name: ")
# print(boston.feature_names)
# 
# ### Lineal regression multiple: I prepare the data
# 
# # I selected the columns 5, 6 and 7 of dataset
# X_multiple = boston.data[:, 5:8]
# print(X_multiple)
# 
# # I define the data corresponding to the tags
# y_multiple = boston.target
# 
# ### Lineal regression multiple implementation
# 
# from sklearn.model_selection import train_test_split
# 
# # I split the data of "train" in train and test for test the algorithm
# X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)
# 
# # I define the algorithm to use
# lr_multiple = linear_model.LinearRegression()
# 
# # I train the model
# lr_multiple.fit(X_train, y_train)
# 
# # I make a prediction
# Y_pred_multiple = lr_multiple.predict(X_test)
# 
# print("Data of Lineal regression model")
# print()
# 
# print("Pending's value or coefficient a: ")
# print(lr_multiple.coef_)
# 
# print("Intersection's value or coeffiecient b: ")
# print(lr_multiple.intercept_)
# 
# print("Model's presicion: ")
# print(lr_multiple.score(X_train, y_train))
# 
# 
#==============================================================================
# Polynomial regression
#==============================================================================
# 
# 
# ### I import the library to use
# import numpy as np
# from sklearn import datasets, linear_model
# import matplotlib.pyplot as plt
# 
# 
# ### Prepare the data
# 
# # I import the data from same library of scikit-learn
# boston = datasets.load_boston()
# print(boston)
# print()
# 
# 
# ### Data understanding
# 
# # I check the information of the dataset
# print("The information about dataset:")
# print(boston.keys())
# print()
# 
# # I verify the characteristic of dataset
# print("The characteristic of dataset: ")
# print(boston.DESCR)
# 
# # I verify the quantity of data what are there in dataset
# print("Quantity of data: ")
# print(boston.data.shape)
# print()
# 
# # I verify the information of columns
# print("Columns names: ")
# print(boston.feature_names)
# 
# 
# ###### Prepare the data: polynomial regression
# 
# # I selected the column 6 of dataset
# X_p = boston.data[:, np.newaxis, 5]
# 
# # I define the data corresponding to the tags
# y_p = boston.target
# 
# # I graphic the corresponding data
# plt.scatter(X_p, y_p)
# plt.show()  
# 
# ### Polynomial regression implementation
# 
# from sklearn.model_selection import train_test_split
# 
# # I split the train data in training and I test the algorithm
# X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_p, y_p, test_size=0.2)
# 
# from sklearn.preprocessing import PolynomialFeatures
# 
# # I define the degree of polynomial
# poli_reg = PolynomialFeatures(degree = 2)
# 
# # Transform the existing characteristics to a characteristics greater degree
# X_train_poli = poli_reg.fit_transform(X_train_p)
# X_test_poli = poli_reg.fit_transform(X_test_p)
# 
# # I define the algorithm to use
# pr = linear_model.LinearRegression()
# 
# # Training the model
# pr.fit(X_train_poli, y_train_p)
# 
# # I realize a prediction
# Y_pred_pr = pr.predict(X_test_poli)
# 
# # I graphich the data together with model
# plt.scatter(X_test_p, y_test_p)
# plt.plot(X_test_p, Y_pred_pr, color="red", linewidth=3)
# plt.show()
# 
# 
# print()
# print("Data of polynomial regression model: ")
# print()
# 
# print("Pending value or coefficient a")
# print(pr.coef_)
# 
# 
# print("Intercept value or coefficient o")
# print(pr.intercept_)
# 
# print("Model's presicion: ")
# print(pr.score(X_train_poli, y_train_p))
#==============================================================================
# Vector of support regression 
#==============================================================================
# 
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
# 
# 
# ### prepare of the data ###
# # Import the data of the same library that scikit-learn
# boston = datasets.load_boston()
# print(boston)
# print()
# 
# ### understanding of data ###
# # Check the information contain in the dataset
# print('Information of the dataset:')
# print(boston.keys())
# print()
# 
# # Check the characteristic of dataset
# print('Characteristic of dataset: ')
# print(boston.DESCR)
# 
# # Check the number of data that's there in the dataset
# print('Number of data:')
# print(boston.data.shape)
# print()
# 
# # Check the information of columns
# print('Columns names: ')
# print(boston.feature_names)
# 
# ### Preparing the vectors support regression
# 
# # Selected the column number 6 of dataset
# X_svr = boston.data[:, np.newaxis, 5]
# 
# # I defined the data corresponding to tags
# y_svr = boston.target
# 
# 
# # Graphic to the corresponding data
# plt.scatter(X_svr, y_svr)
# plt.show()
# 
# 
# ### Implementation of vectors support regression
# from sklearn.model_selection import train_test_split 
# 
# # I split the data "train" in training and test for test the algorithm
# X_train, X_test, y_train, y_test = train_test_split(X_svr, y_svr, test_size=0.2)
# 
# from sklearn.svm import SVR
# 
# # I define the algorithm to use
# svr = SVR(kernel = 'linear', C=1.0, epsilon=0.2)
# 
# # I train the model
# svr.fit(X_train, y_train)
# 
# # I realice a prediction
# Y_pred = svr.predict(X_test)
# 
# # I graphic the data together with the model 
# plt.scatter(X_test, y_test)
# plt.plot(X_test, Y_pred, color='red', linewidth=3)
# plt.show()
# 
# print()
# print('Data of model vectors support regression')
# print()
# 
# 
# print('Presicion of model: ')
# print(svr.score(X_train, y_train))
# 
#==============================================================================
# Decision Tree Regression
#==============================================================================
# 
# # I import the libraties to use
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
# 
# ### Prepare the data ###
# 
# # I import the same data of scikit-learn library
# boston = datasets.load_boston()
# print(boston)
# print()
# 
# 
# ### Data understanding ###
# 
# # I check the information contain in dataset
# print('Information of dataset: ')
# print(boston.keys())
# print()
# 
# # I verify the dataset's characteristics
# print("Dataset's characteristic")
# print(boston.DESCR)
# 
# # I check the number of data that's there in dataset
# print("Data's number:")
# print(boston.data.shape)
# print()
# 
# # I check the information of columns
# print("Columns's name: ")
# print(boston.feature_names)
# 
# 
# ### Prepare the data of the Decision Tree Regression ###
# 
# # I select only the column 6 of dataset
# X_adr = boston.data[:, np.newaxis, 5]
# 
# # I define the data corresponding of the tags
# y_adr = boston.target
# 
# # I graphic the corresponding data
# plt.scatter(X_adr, y_adr)
# plt.show()
# 
# 
# ### Implementation of Decision Tree Regression ###
# 
# from sklearn.model_selection import train_test_split
# 
# # I split the data of "train" in train and test for to probe the algorithms
# X_train, X_test, y_train, y_test = train_test_split(X_adr, y_adr, test_size = 0.2)
# 
# from sklearn.tree import DecisionTreeRegressor
# 
# # I define the algorithms to use
# adr = DecisionTreeRegressor(max_depth=5)
# 
# # I train the model
# adr.fit(X_train, y_train)
# 
# # I realice a prediction
# Y_pred = adr.predict(X_test)
# 
# # I graphic the test's data togheter with the prediction
# X_grid = np.arange(min(X_test), max(X_test), 0.1)
# X_grid = X_grid.reshape((len(X_grid), 1))
# plt.scatter(X_test, y_test)
# plt.plot(X_grid, adr.predict(X_grid), color='red', linewidth=3)
# plt.show()
# 
# print('Data of Decision Tree Regression')
# print()
# 
# print('Model presicion')
# print(adr.score(X_train, y_train))
#==============================================================================
# Random Forest Regression

### Libraries to use ###

# I import the libraries
# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
# 
# 
# ### Prerare the data ###
# 
# # I import the data from the same library scikit-learn
# boston = datasets.load_boston()
# print(boston)
# print()
# 
# 
# ### Understanding the data ###
# 
# # I check the information contain in the dataset
# print('Information of dataset: ')
# print(boston.keys())
# print()
# 
# # I check the characteristic of dataset
# print('Characteristic of dataset: ')
# print(boston.DESCR)
# 
# # I check the number of data is there in dataset
# print('Number of data: ')
# print(boston.data.shape)
# print()
# 
# # I check the information of columns
# print('Column names:')
# print(boston.feature_names)
# 
# 
# ### Prepare de data of Random Forecast Regression ###
# 
# # Select the column 6 of dataset
# X_bar = boston.data[:, np.newaxis, 5]
# 
# # Define the data corresponding to dataset
# y_bar = boston.target
# 
# # Graphic the corresponding data
# plt.scatter(X_bar, y_bar)
# plt.show()
# 
# 
# ### Implementation of Random Forecast Regression ###
# 
# from sklearn.model_selection import train_test_split
# 
# # I split the data "train" between training and test for to check
# # the next algorithms
# 
# X_train, X_test, y_train, y_test = train_test_split(X_bar,y_bar,test_size=0.2)
# 
# from sklearn.ensemble import RandomForestRegressor
# 
# # I define the algorithm to use
# bar = RandomForestRegressor(n_estimators = 300, max_depth = 8)
# 
# # I train the model
# bar.fit(X_train, y_train)
# 
# # I realice a prediction
# Y_pred = bar.predict(X_test)
# 
# # Graphic the test data togheter with the prediction data
# X_grid = np.arange(min(X_test), max(X_test), 0.1)
# X_grid = X_grid.reshape((len(X_grid), 1))
# plt.scatter(X_test, y_test)
# plt.plot(X_grid, bar.predict(X_grid), color='red', linewidth=3)
# plt.show()
# 
# 
# print('Information about the model of Random Forecast Regression')
# print()
# 
# print('Precision of model: ')
# print(bar.score(X_train, y_train))
# =============================================================================

# =============================================================================
# x = 2
# 
# a = [x**3-1 for xi in range(7)]
# print(a)
# =============================================================================
