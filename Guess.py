# # core application logic itself (menu display, user input, scoring logic, etc).

# import os  # to clear the screen

# class Guess:

#     def clearScreen():
#         # clear the screen
#         os.system('cls');

#     def displayMenu():
#         # game intro
#         print("++");
#         print("++ The great guessing game");
#         print("++");
#         print("Current Guess: ");
#         print("Letters guessed");
#         print("g = guess, t = tell me, l for a letter, and q to quit");
#         print("Enter Option: ");

#     def displayLettersGuessed():


class Guess:
    def __init__(self):
        self.currentOption = None
        self.optionDict = {
            "g": "guess",
            "t": "tell me",
            "l": "for a letter",
            "q": "to quit",
        }

    def displayOpeningMessage(self):
        print("++\n++The great guessing game\n++")

    def displayGameOptions(self):
        # print("Game Options:")
        for key, value in self.optionDict.items():
            print(f"{key}: {value}", end=" ")

    def displayEnterOption(self):
        print("Enter your option:")

    def askUserForOption(self):
        self.currentOption = input().lower()
        self.validateOptionInput()

    def validateOptionInput(self):
        while self.currentOption not in self.optionDict:
            print("Invalid option. Please re-enter:")
            self.displayEnterOption()
            self.currentOption = input().lower()

    def displayEnterLetter(self):
        print("Enter a letter:")

    def askUserForLetter(self, gameObject):
        self.currentGuessedLetter = input().lower()
        gameObject.lettersGuessedList.append(self.currentGuessedLetter)

    def feedbackForCurrentGuess(self, gameObject):
        if self.currentGuessedLetter not in gameObject.targetWord:
            print("@@\n@@FEEDBACK: Not a single match, genius\n@@")
        else:
            print("@@\n@@FEEDBACK: Woo hoo, you found 1 letters\n@@")

    # TODO FIXME LEARN MORE OR UPDATE
    def displayLettersGuessed(self, gameObject):
        print("Letters Guessed: ", ", ".join(gameObject.lettersGuessedList))

    def displayCurrentWordGuessed(self, gameObject):
        print("Current Word: ", " ".join(gameObject.currentGuessedWord))

    def displayTargetWord(self, gameObject):
        print(f"Current Word: {gameObject.targetWord}")

