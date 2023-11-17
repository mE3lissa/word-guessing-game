# disk I/O (i.e., the word file) and random selection of the word for a new game.

import random   # to generate a random value from the list

class StringDatabase:
    
    def __init__(self, fileName):
        self.wordsList = self.loadWords(fileName);
        
    def loadWords(self, fileName):
        try:
            with open(fileName, 'rt') as file:
                words = [word.strip().lower() for word in file.readlines()]
            return words
        except FileNotFoundError:
            print(f"Error: File '{fileName}' not found.")
            exit(1)
        
    def getRandomWord(self):
        return random.choice(self.wordsList);

        
