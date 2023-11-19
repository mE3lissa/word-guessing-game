class Game:
    def __init__(self, wordToGuess):
        self.targetWord = wordToGuess.lower()
        self.lettersGuessedList = []
        self.wordsGuessedList = []
        self.lettersMissedList = []
        self.currentGuessedWord = [
            "_" if char.isalpha() else char for char in self.targetWord
        ]
        self.gameScore = 0
        self.currentGuessedLetter = None
        self.successStatus = False
        self.numOfBadGuesses = 0
        self.guessInput = None
        self.letterFrequencyDict = {
            "a": 8.17,
            "b": 1.49,
            "c": 2.78,
            "d": 4.25,
            "e": 12.70,
            "f": 2.23,
            "g": 2.02,
            "h": 6.09,
            "i": 6.97,
            "j": 0.15,
            "k": 0.77,
            "l": 4.03,
            "m": 2.41,
            "n": 6.75,
            "o": 7.51,
            "p": 1.93,
            "q": 0.10,
            "r": 5.99,
            "s": 6.33,
            "t": 9.06,
            "u": 2.76,
            "v": 0.98,
            "w": 2.36,
            "x": 0.15,
            "y": 1.97,
            "z": 0.07,
        }
