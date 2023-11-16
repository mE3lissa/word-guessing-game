# #very simply non object oriented file. It simply parses the command line parameter and starts the guessing game.

# import sys  # to parse the command line parameter
# import Guess;
# import Game;
# import StringDatabase;


# def main():
#     if "play" in sys.argv:

#         # start the guess
#         print("play now");

#     elif "test" in sys.argv:

#         # start the test
#         print("test now");


# # run main if this file is main
# if __name__ == "__main__":
#     main();


# #run all files
# #python3 words.py test (words.py is the driver)

from Guess import Guess 
from Game import Game

if __name__ == "__main__":
    # Create instances
    guessGame = Guess()
    wordGame = Game("python")

    # Call methods in sequence
    guessGame.displayOpeningMessage()
    guessGame.displayTargetWord(wordGame)
    guessGame.displayCurrentWordGuessed(wordGame)
    guessGame.displayLettersGuessed(wordGame)

    guessGame.displayGameOptions()
    guessGame.displayEnterOption()
    guessGame.askUserForOption()
    guessGame.validateOptionInput()

    # if option entered is g then call displayEnterWord then ask for word
    # if option entered is l then call displayEnterletter then ask for letter
    # if option entered is t 

    guessGame.displayEnterLetter()
    guessGame.askUserForLetter(wordGame)
    guessGame.feedbackForCurrentGuess(wordGame)
