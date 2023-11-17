# # core application logic itself (menu display, user input, scoring logic, etc).

import os
from Game import Game

class Guess:
    def __init__(self):
        self.currentOption = None
        self.currentGame = None;
        self.gamesPlayed = []
        self.optionDict = {
            "g": "guess",
            "t": "tell me",
            "l": "for a letter",
            "q": "to quit",
        }

    def displayOpeningMessage(self):
        os.system("clear" if os.name == "posix" else "cls")  # Clear screen
        print("++\n++The great guessing game\n++")

    def displayGameOptions(self):
        # print("Game Options:")
        for key, value in self.optionDict.items():
            print(f"{key}: {value}", end=" ")

    def displayEnterLetter(self):
        print("Enter a letter:")

    def askUserForLetter(self, gameObject):
        self.currentGuessedLetter = input().lower()
        gameObject.lettersGuessedList.append(self.currentGuessedLetter)

    def feedbackForCurrentGuessedLetter(self, gameObject):
        if gameObject.currentGuessedLetter in gameObject.targetWord:
            print("@@\n@@FEEDBACK: Woo hoo, you found 1 letters\n@@")
        else:
            print("@@\n@@FEEDBACK: Not a single match, genius\n@@")

    def feedbackForCurrentGuessedWord(self, gameObject):
        if gameObject.currentGuessedWord in gameObject.targetWord:
            print("@@\n@@FEEDBACK: You're right, Einstein!\n@@")
        else:
            print("@@\n@@FEEDBACK: Try again, Loser!\n@@")

    ### todo fixme LEARN MORE OR UPDATE ###

    def displayLettersGuessed(self, gameObject):
        print("Letters Guessed: ", ", ".join(gameObject.lettersGuessedList))

    def displayCurrentWordGuessed(self, gameObject):
        print("Current Word: ", " ".join(gameObject.currentGuessedWord))

    def displayTargetWord(self, mode, gameObject):
        if mode == "test":
            print(f"Current Word: {gameObject.targetWord}")

    def processCurrentGuessedLetter(self, gameObject):
        if gameObject.currentGuessedLetter.isalpha():
            if gameObject.currentGuessedLetter in gameObject.lettersGuessedList or gameObject.currentGuessedLetter in gameObject.lettersMissedList:
                print("You already guessed that letter. Try a different one.")
            elif gameObject.currentGuessedLetter in gameObject.targetWord:
                self.updateCurrentGuessedWord()
                self.lettersGuessedList.append(self.currentGuessedLetter)
                self.updateGameStatus()
            else:
                self.numOfBadGuesses += 1
                self.lettersMissedList.append(self.currentGuessedLetter)
        else:
            print("Invalid input. Please enter a valid letter.")

    def updateCurrentGuessedWord(self):
        for index, char in enumerate(self.targetWord):
            if char.isalpha() and char == self.currentGuessedLetter:
                self.currentGuessedWord[index] = char
                
    def playGame(self, wordDatabase, mode):
        while True:
            self.currentGame = Game(wordDatabase.getRandomWord())
            
            while True:
                self.displayOpeningMessage()
                self.displayTargetWord(mode, self.currentGame)
                self.displayCurrentWordGuessed(self.currentGame)
                self.displayLettersGuessed(self.currentGame)
                self.displayGameOptions()

                self.currentOption = input("Enter Option: ").strip().lower()

                if self.currentOption == 'g':
                    self.currentGame.guessInput = input("Make your guess: ").strip().lower()
                    self.feedbackForCurrentGuessedWord(self.currentGame)

                elif self.currentOption == 't':
                    self.currentGame.give_up()
                    break

                elif self.currentOption == 'l':
                    self.currentGame.currentGuessedLetter = input("Enter a letter: ").strip().lower()
                    self.processCurrentGuessedLetter(self.currentGame)

                elif self.currentOption == 'q':
                    self.games_played.append(self.currentGame)
                    print("Game Over. Thanks for playing!")
                    self.display_final_report()
                    return

                else:
                    print("Invalid option. Please re-enter: ")

# # Example usage:
# class Game:
#     def __init__(self, targetWord):
#         self.targetWord = targetWord
#         self.currentGuessedWord = ["_" for _ in targetWord]
#         self.lettersGuessedList = []


# # Instantiate Guess class
# guessGame = Guess()
# guessGame.optionDict = {'1': 'Option 1', '2': 'Option 2', '3': 'Option 3'}

# # Example gameplay loop
# guessGame.displayOpeningMessage()
# guessGame.displayGameOptions()
# guessGame.displayEnterOption()
# guessGame.askUserForOption()

# # Assume the selected option is related to a word guessing game
# wordGame = Game("python")

# guessGame.displayEnterLetter()
# guessGame.askUserForLetter(wordGame)
# guessGame.feedbackForCurrentGuess(wordGame)
# guessGame.displayLettersGuessed(wordGame)
# guessGame.displayCurrentWordGuessed(wordGame)
