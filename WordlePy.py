while True:

    try:

        print("Welcome to Wordle but in python.")
        print(" ")
        print("If you would like to know the rules, input '1'.")
        print("If you would like to play, input '2'.")
        print(" ")
        user_input = int(input("Enter your selected option:"))

        if user_input == 1:
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print("You have to guess the Wordle in six goes or less.")
            print("Every word you enter must be in the word list.")
            print("A correct letter turns green.")
            print("A correct letter in the wrong place turns yellow.")                
            print("An incorrect letter turns gray.")
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
        

#main game goes here...


