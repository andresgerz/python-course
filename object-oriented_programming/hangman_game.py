#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:30:54 2019

@author: andres
"""

# Make the hangman game, write the letters that one thinks 


class Hangman_game():
    
    def __init__(self):
        self.word = input("Word to guess: ")
        self.nro_letters = len(self.word)
        self.nro_lifes = int(input("Number of lifes: "))
        self.correct_answer_nro = 0
        
    def verification(self):
        
        while(self.nro_lifes > 0):
            self.a_letter = input("Put a letter: ")
            
            if(self.word.find(self.a_letter) >= 0):
                self.correct_answer_nro += 1
            else:
                self.nro_lifes -= 1
                    
            if(self.nro_letters == self.correct_answer_nro):
                print("=================")
                print("| YOU WON IT!!! |")
                print("=================")
                break
                
            print("Lifes: ", self.nro_lifes)
        
        if(self.nro_lifes == 0):
            print("GAME OVER")
        
    def printing_result(self):
        print("\n========== GAME ===============================")
        print("Number of letters: " + str(self.nro_letters))
        print("Number of lifes: " + str(self.nro_lifes))
        print("Word: " + self.word)
        print("Correct answers nro: " + str(self.correct_answer_nro))
        print("=============================================")

        
        
game1 = Hangman_game()

game1.verification()

game1.printing_result()