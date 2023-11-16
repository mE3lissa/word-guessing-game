# core application logic itself (menu display, user input, scoring logic, etc).

import os  # to clear the screen

class Guess:

    def clearScreen():
        # clear the screen
        os.system('cls');
    
    def displayMenu():
        # game intro
        print("++");
        print("++ The great guessing game");
        print("++");
        print("Current Guess: ");
        print("Letters guessed");
        print("g = guess, t = tell me, l for a letter, and q to quit");
        print("Enter Option: ");

    def displayLettersGuessed():
        
    