import random   


class StringDatabase:
    
    def __init__(self, fileName):
        self.wordsList = self.loadWords(fileName);
        

    def loadWords(self, fileName):
        try:
            with open(fileName, 'rt') as file:
                words = [word.strip().lower() for line in file for word in line.split()]
            return words
        except FileNotFoundError:
            print(f"Error: File '{fileName}' not found.")
            exit(1)
        

    def getRandomWord(self):
        return random.choice(self.wordsList);

        
