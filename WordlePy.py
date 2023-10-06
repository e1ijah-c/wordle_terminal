import sys
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

with open("Wordle_Dictionary.txt") as file:
    words = file.readlines()

    for word in words:
        wordbank.append(word.strip('\n'))

def main():
    start()

def game():
    n = 0
    i = randint(0, len(wordbank))
    wordle = wordbank[i]

    for letter in wordle:
        wordle_char.append(letter)

    #print(wordle)

    for t in range(turns):

        guess_char.clear()

        while True:
            try:
                print(" ")
                guess = input("Enter your " + num_terms[n] + " guess: ")
                
                if guess not in wordbank or len(guess) > 5:
                    print(" ")
                    print(Style.BRIGHT + Fore.RED + "Invalid input!")
                    print(Style.RESET_ALL)
                
                if len(guess) == 5:
                    if guess in wordbank:
                        for g in guess:
                            guess_char.append(g)
                        n += 1
                        break

            except ValueError:
                print(" ")
                print(Style.BRIGHT + Fore.RED + "Invalid input!")
                print(Style.RESET_ALL)
        
        for c in range(len(wordle_char)):



            if guess_char[c] == wordle_char[c]:
                print(Fore.GREEN + guess_char[c], end=" ")

            elif guess_char[c] in wordle_char:
                print(Fore.YELLOW + guess_char[c], end=" ")
            
            if guess_char[c] not in wordle_char:
                print(Style.DIM + Fore.WHITE + guess_char[c], end=" ")
                print(Style.RESET_ALL, end="")


            if c >= len(wordle_char):
                c = 0
        
        print(" ")
        print(Style.RESET_ALL)

        if guess_char == wordle_char:

            n = 0
            wordle_char.clear()

            print(" ")
            print("Congratulations, you got it!")
            print("Would you like to play again?")

            while True:
                try:
                    print(" ")
                    print("If you would like to quit, input '1'.")
                    print("If you would like to play again, input '2'.")
                    print(" ")
                    ans = int(input("Enter your selected option: "))

                    if ans == 1:
                        sys.exit()

                    if ans == 2:
                        game()

                except ValueError:
                    print(" ")
                    print(Style.BRIGHT + Fore.RED + "Invalid input!")
                    print(Style.RESET_ALL)
    
    n = 0
    wordle_char.clear()

    print(" ")
    print("Sorry you're out of tries, the word was " + wordle + ".")
    print(" ")
    print("Would you like to play again?")

    while True:
        try:
            print(" ")
            print("If you would like to quit, input '1'.")
            print("If you would like to play again, input '2'.")
            print(" ")
            ans = int(input("Enter your selected option: "))

            if ans == 1:
                sys.exit()

            if ans == 2:
                game()

        except ValueError:
            print(" ")
            print(Style.BRIGHT + Fore.RED + "Invalid input!")
            print(Style.RESET_ALL)
       

def start():
    while True:

        try:

            print(" ")
            print(Fore.CYAN + Style.BRIGHT + "Welcome to Wordle but in python.")
            print(Style.RESET_ALL)

            print("If you would like to know the rules, input ", end="") 
            print(Fore.MAGENTA + "'1'.", end="")
            print(Style.RESET_ALL)
            
            
            print("If you would like to play, input ", end="")
            print(Fore.MAGENTA + "'2'.", end="")
            print(Style.RESET_ALL)
            
            
            print("If you would like to quit, input ", end="")
            print(Fore.MAGENTA + "'3'.", end="")
            print(Style.RESET_ALL)
            
            print(" ")
            user_input = int(input("Enter your selected option: "))

            if user_input == 1:
                print("")
                print("")

                print("1. You have to guess the Wordle in 6 goes or less.")
                print(" ")
                print("2. Every word you enter must be in the word list.")
                print(Style.RESET_ALL)

                print("3. A correct letter turns ", end="")
                print(Fore.GREEN + "GREEN")
                print(Style.RESET_ALL)
                
                print("4. A correct letter in the wrong place turns ", end="")  
                print(Fore.YELLOW + "YELLOW")
                print(Style.RESET_ALL)              
                
                print("5. An incorrect letter turns ", end="")
                print(Style.DIM + Fore.WHITE + "GREY")
                print(Style.RESET_ALL)

                print("6. Letters can be used more than once.")
                print("")
                print("7. Answers are never plurals.")
                print(Style.RESET_ALL)
                print(Style.BRIGHT + Fore.MAGENTA + "Good Luck ;)")
                print(Style.RESET_ALL)

                game()


            if user_input == 2:

                game()
            
            if user_input == 3:
                sys.exit()

        except ValueError:
            print(" ")
            print(Style.BRIGHT + Fore.RED + "Invalid input!")
            print(Style.RESET_ALL)

    return
    
    
while True:
    main()

            
