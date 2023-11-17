# #very simply non object oriented file. It simply parses the command line parameter and starts the guessing game.

import sys
from Guess import Guess 
from Game import Game
from StringDatabase import StringDatabase

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["play", "test"]:
        print("Usage: python3 words.py [play/test]")
        sys.exit(1)

    mode = sys.argv[1].strip().lower()

    # Initialize StringDatabase
    wordDatabase = StringDatabase("four_letters.txt")

    # Initialize Guess with the mode
    guessGame = Guess()

    # Starts the guessing game
    guessGame.playGame(wordDatabase, mode)

if __name__ == "__main__":
    main()

