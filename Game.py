# # maintain information about a specific game (needed for the final report)

class Game:
    def __init__(self, wordToGuess):
        self.letterFrequencyDict = {
            "a": "8.17",
            "b": "1.49",
            "c": "2.78",
            "d": "4.25",
            "e": "12.70",
            "f": "2.23",
            "g": "2.02",
            "h": "6.09",
            "i": "6.97",
            "j": "0.15",
            "k": "0.77",
            "l": "4.03",
            "m": "2.41",
            "n": "6.75",
            "o": "7.51",
            "p": "1.93",
            "q": "0.10",
            "r": "5.99",
            "s": "6.33",
            "t": "9.06",
            "u": "2.76",
            "v": "0.98",
            "w": "2.36",
            "x": "0.15",
            "y": "1.97",
            "z": "0.07",
        }
        self.targetWord = wordToGuess.lower()
        self.lettersGuessedList = []
        self.wordsGuessedList = []
        self.lettersMissedList = []
        self.currentGuessedWord = [
            "_" if char.isalpha() else char for char in self.targetWord
        ]
        self.finalScore = 0
        self.currentGuessedLetter = None
        self.successStatus = False
        self.numOfBadGuesses = 1
        self.guessInput = None
        


    # # implement
    # def giveUp(self):
    #     self.finalScore -= self.calculateRemainingLettersPenalty() 


    # # implement    
    # def calculateRemainingLettersPenalty(self):


    # def updateLetterFrequencyDict(self):
    #     for char in self.targetWord:
    #         if char.isalpha():
    #             self.letterFrequencyDict[char] = self.letterFrequencyDict.get(char, 0) + 1


    # def updateFinalScore(self):
    #     self.finalScore = max(0, len(self.targetWord) - self.numOfBadGuesses)

    # def displayGameStatus(self):
    #     if self.successStatus:
    #         print("Congratulations! You guessed the word.")
    #     else:
    #         print(f"Sorry, you've run out of attempts. The correct word was '{self.targetWord}'.")

    # def displayCurrentGuessedWord(self):
    #     print("Current Word: ", " ".join(self.currentGuessedWord))

    # def displayFinalScore(self):
    #     print(f"Final Score: {self.finalScore}")

    # def displayNumOfBadGuesses(self):
    #     print(f"Number of Incorrect Guesses: {self.numOfBadGuesses}")

    # def displayLetterFrequency(self):
    #     print("Letter Frequency:")
    #     for letter, frequency in self.letterFrequencyDict.items():
    #         print(f"{letter}: {frequency}")

 
  