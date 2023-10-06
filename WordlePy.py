import random
from random import randint
import colorama
from colorama import Fore, Style


wordbank = []
wordle_char = []
guess_char = []
num_terms = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "LAST"]

guess = ''
turns = 6
n = 0


with open("Wordle_Dictionary.txt") as file:
    words = file.readlines()

    for word in words:
        wordbank.append(word.strip('\n'))

while True:

    try:

        print(Fore.RED + "Welcome to Wordle but in python.")
        print(" ")
        print("If you would like to know the rules, input '1'.")
        print("If you would like to play, input '2'.")
        print(" ")
        user_input = int(input("Enter your selected option: "))

        if user_input == 1:
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print("You have to guess the Wordle in 6 goes or less.")
            print("Every word you enter must be in the word list.")
            print("A correct letter turns GREEN.")
            print("A correct letter in the wrong place turns YELLOW.")                
            print("An incorrect letter turns GRAY.")
            print("Letters can be used more than once.")
            print("Answers are never plurals.")
            print(" ")
            print("Good Luck!")
            print(" ")

            break

        if user_input == 2:
            break

    except ValueError:
        print(" ")
        print("Invalid input!")
        print(" ")
        
#main game goes here.............................................................................

i = randint(0, len(wordbank))
wordle = wordbank[i]

for letter in wordle:
    wordle_char.append(letter)
#print(wordle)

for t in range(turns):

    while True:
        try:
            print(" ")
            guess = input("Enter your " + num_terms[n] + " guess: ")

            for g in guess:
                guess_char.append(g)
            
            if guess not in wordbank or len(guess) > 5:
                print(" ")
                print("Invalid input!")
                print(" ")
            
            if len(guess) == 5:
                if guess in wordbank:
                    n += 1
                    break


        except ValueError:
            print(" ")
            print("Invalid input!")
            print(" ")
    
    for i in range(0, 5):

        if guess_char[i] == wordle_char[i]:
            print(colored(guess_char[i], 'green'), end=" ")