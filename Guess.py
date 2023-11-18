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

    def clearScreen(self):
        os.system("clear" if os.name == "posix" else "cls")


    def displayOpeningMessage(self):
        self.clearScreen()
        print("++\n++ The great guessing game\n++\n")
    

    def displayGameReportMessage(self):
        self.clearScreen()
        print("++\n++ Game Report\n++\n")


    def displayGameOptions(self):
        # print("Game Options:")
        for key, value in self.optionDict.items():
            print(f"{key} = {value}", end="  ")


    def feedbackForCurrentGuessedLetter(self, gameObject, countOfMatchedLetters):
        if gameObject.currentGuessedLetter in gameObject.targetWord:
            print(f"\n@@\n@@ FEEDBACK: Woo hoo, you found {countOfMatchedLetters} letters\n@@")
        else:
            print("\n@@\n@@ FEEDBACK: Not a single match, genius\n@@")


    def feedbackForGuessInput(self, gameObject):    #need to fix. error: gameObject.guessInput is a list instead of a string.
        if gameObject.guessInput == gameObject.targetWord:
            print("\n@@\n@@ FEEDBACK: You're right, Einstein!\n@@")
            return True
        else:
            print("\n@@\n@@ FEEDBACK: Try again, Loser!\n@@")
            return False
        

    def displayLettersGuessed(self, gameObject):
        print("Letters Guessed: ", ", ".join(gameObject.lettersGuessedList), end="\n\n")


    def displayCurrentWordGuessed(self, gameObject):
        print("Current Guess: ", " ".join(gameObject.currentGuessedWord))


    def displayTargetWord(self, mode, gameObject):
        if mode == "test":
            print(f"Current Word: {gameObject.targetWord}")


    def updateLettersGuessedList(self, gameObject):
        gameObject.lettersGuessedList.append(gameObject.currentGuessedLetter)


    def updateWordsGuessedList(self, gameObject):
        gameObject.wordsGuessedList.append(gameObject.guessInput)


    def updateSuccessStatus(self, gameObject):
        if "_" not in gameObject.currentGuessedWord or gameObject.guessInput == gameObject.targetWord:
            gameObject.successStatus = True


    def processGuessInput(self, gameObject):
        if gameObject.guessInput.isalpha():
            if gameObject.guessInput in gameObject.wordsGuessedList:
                print("\n@@\n@@ FEEDBACK: You already guessed that word. Try a different one\n@@")

            elif gameObject.guessInput == gameObject.targetWord:
                self.feedbackForGuessInput(gameObject)
                self.updateSuccessStatus(gameObject)
                
            else:
                self.feedbackForGuessInput(gameObject)
                self.updateWordsGuessedList(gameObject)
                gameObject.numOfBadGuesses += 1
                
        else:
            print("\n@@\n@@ FEEDBACK: Invalid input. Please enter a valid word\n@@")


    def processCurrentGuessedLetter(self, gameObject):
        if gameObject.currentGuessedLetter.isalpha() and len(gameObject.currentGuessedLetter) == 1:
            if gameObject.currentGuessedLetter in gameObject.lettersGuessedList or gameObject.currentGuessedLetter in gameObject.lettersMissedList: # what the the lettersMissedList????
                print("\n@@\n@@ FEEDBACK: You already guessed that letter. Try a different one\n@@")

            elif gameObject.currentGuessedLetter in gameObject.targetWord:
                self.updateCurrentGuessedWord(gameObject)
                self.updateLettersGuessedList(gameObject)
                self.updateSuccessStatus(gameObject)
               
            else:
                self.feedbackForCurrentGuessedLetter(gameObject, 0)
                self.updateLettersGuessedList(gameObject)
                gameObject.lettersMissedList.append(gameObject.currentGuessedLetter)
        else:
            print("\n@@\n@@ FEEDBACK: Invalid input. Please enter a valid letter\n@@")


    def updateCurrentGuessedWord(self, gameObject):
        countOfMatchedLetters = 0
        for index, char in enumerate(gameObject.targetWord):
            if char.isalpha() and char == gameObject.currentGuessedLetter:
                gameObject.currentGuessedWord[index] = char
                countOfMatchedLetters += 1
        self.feedbackForCurrentGuessedLetter(gameObject, countOfMatchedLetters)
        

    def processTellMeOption(self, gameObject):
        print(f"\n@@\n@@ FEEDBACK: You really should have guessed this...'{gameObject.targetWord}'\n@@")


    def validateCurrentOption(self):
        while self.currentOption not in self.optionDict:
            self.currentOption = input("\nInvalid option. Please re-enter: ").strip().lower()


    def pressAnyKeyToContinue(self):
        input("\nPress any key to continue...")
    

    def calculateRemainingLettersFrequency(self, gameObject):
        frequency = 0.0
        for index, char in enumerate(gameObject.currentGuessedWord):
            if char == "_" and gameObject.targetWord[index] in gameObject.letterFrequencyDict:
                frequency += gameObject.letterFrequencyDict[gameObject.targetWord[index]]
        return frequency


    def calculateFinalScore(self, gameObject):
        if gameObject.successStatus:
            divideFrequencyBy = 1 if len(gameObject.lettersGuessedList) == 0 else len(gameObject.lettersGuessedList)    # avoid divisionByZeroError 
            gameObject.finalScore = (self.calculateRemainingLettersFrequency(gameObject)/divideFrequencyBy) * ( 1 - (0.1 * gameObject.numOfBadGuesses))
        else:
            gameObject.finalScore = -(self.calculateRemainingLettersFrequency(gameObject))


    def displayFinalReport(self, gameObject):
        self.displayGameReportMessage()
        for index, gameObject in enumerate(self.gamesPlayed):
            print(f"{index}  {gameObject.targetWord}  {gameObject.successStatus}  {gameObject.numOfBadGuesses}  {len(gameObject.lettersGuessedList)}  {format((gameObject.finalScore), ".2f")}" )


    def playGame(self, wordDatabase, mode):
        while True:
            self.currentGame = Game(wordDatabase.getRandomWord())
            
            while True:
                self.displayOpeningMessage()
                self.displayTargetWord(mode, self.currentGame)
                self.displayCurrentWordGuessed(self.currentGame)
                self.displayLettersGuessed(self.currentGame)
                self.displayGameOptions()

                self.currentOption = input("\n\nEnter Option: ").strip().lower()
                self.validateCurrentOption()

                if self.currentOption == 'g':
                    self.currentGame.guessInput = input("\nMake your guess: ").strip().lower()
                    self.processGuessInput(self.currentGame)
        
                    if self.currentGame.successStatus:
                        self.calculateFinalScore(self.currentGame)
                        self.gamesPlayed.append(self.currentGame)
                        self.pressAnyKeyToContinue()
                        break

                elif self.currentOption == 't':
                    self.processTellMeOption(self.currentGame)
                    self.calculateFinalScore(self.currentGame)
                    self.gamesPlayed.append(self.currentGame)
                    self.pressAnyKeyToContinue()
                    break

                elif self.currentOption == 'l':
                    self.currentGame.currentGuessedLetter = input("\nEnter a letter: ").strip().lower()
                    self.processCurrentGuessedLetter(self.currentGame)

                    if self.currentGame.successStatus:
                        print("\n@@\n@@ FEEDBACK: Congratulations, Einstein. You guessed the word!\n@@")
                        self.calculateFinalScore(self.currentGame)
                        self.gamesPlayed.append(self.currentGame)
                        self.pressAnyKeyToContinue()
                        break

                elif self.currentOption == 'q':
                    self.displayFinalReport(self.currentGame)
                    return
                
                self.pressAnyKeyToContinue()