#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:49:43 2019

@author: andres
"""
import random, sched, time


class Warriors():
    
    def __init__(self, name, region, warriors_nro):
        self.name = name
        self.region = region
        self.warriors_nro = warriors_nro

    def printing(self):
        self
        

class Kingdom():
    
    def __init__(self, king_name, kingdom_name, capital_name, titles, words, soldiers_nro):
        self.king_name = king_name
        self.kingdom_name = kingdom_name
        self.capital_name = capital_name
        self.titles = titles
        self.words = words
        self.soldiers_nro = soldiers_nro
    
    def printing(self):
        print("𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇",
              "\nKingdom name: ", self.kingdom_name,
              "\nKing name: ", self.king_name,
              "\nCapital name: ", self.capital_name,
              "\ntitles: ", self.titles,
              "\nWords: ", self.words, "\n")

class Stark(Kingdom):
    
    def __init__(self):
        
        super().__init__("Stark", "Ned Stark", "Winterfell", "NA","NA", 20000)
        

class Lannister(Kingdom):
    
    def __init__(self):
        
        super().__init__("Lannister", "Cersei Lannister", "King's Landing", 
             "NA", "NA", 20000)


class Greyjoy(Kingdom):
    
    def __init__(self):
        
        super().__init__("Greyjoy", "Yara Greyjoy", "Iron Island", 
             ["Lords of the Iron Slands", "Lord Reapers of Pyke", 
              "Sons of the sea wind", "Kings of salt and rock"], 
             ["We do not sow", "What is dead may never die"], 5000)
        
class Targaryen(Kingdom):

    def __init__(self, dragons_nro, allies):
        
        super().__init__("Targaryen", "Daenerys Targaryen", "NA",
             ["Lords of dragonstone", "Kings of the Andals, the Rhoynar and the First Men",
              "Protectors of the seven kingdoms"],"Fire and blood", 100000)
        self.dragons_nro = dragons_nro
        self.allies = allies
    
    def printing(self):
        
        super().printing()
        print("Allies: ", self.allies,
              "\nNumber of dragons: ", self.dragons_nro, "\n")
        


# white walkers, dothraki, others
class White_walker(Warriors):
    
    def __init__(self):
        super().__init__("White walker", "Winter?", 100000)
    
    def printing(self):
        
        print("𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇𐍇",
              "\nName: ", self.name,
              "\nRegion:", self.region,
              "\nSoldiers: ", self.warriors_nro)
        

class Do_war():
    
        
        
    
    print("\n\nFighting...")
    
     
    
    s = sched.scheduler(time.time, time.sleep)
    def results(sc):
        
        nro_soldiers = White_walker().warriors_nro
        nro_soldiers2 = Stark().soldiers_nro
        
        print(
              White_walker().name, ": ", nro_soldiers - random.randint(0, nro_soldiers),
              "\n", Stark().kingdom_name, ": ", nro_soldiers2 - random.randint(0, nro_soldiers2),
              "\n"
              )
        
        if (nro_soldiers > nro_soldiers2):
            print(White_walker().name,"won!")
        else:
            print(Stark().kingdom_name, "won!")
                
        #s.enter(5, 1, results, (sc,) recursive function 
     
    s.enter(5, 1, results, (s,))
    s.run()
    

stark = Stark()
stark.printing()

lannister = Lannister()
lannister.printing()

greyjoy = Greyjoy()
greyjoy.printing()

targaryen = Targaryen(3, ["Dothraki"])
targaryen.printing()

white_walker = White_walker()
white_walker.printing()
war = Do_war()

print(White_walker().name)