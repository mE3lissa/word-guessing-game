# disk I/O (i.e., the word file) and random selection of the word for a new game.

import random   # to generate a random value from the list



class StringDatabase:
    
    def __init__(self, fileName):
        self.words = self.readWordsFromFile(filePath);
        
    def readWordsFromFile(self, fileName):
    
        # list to store 4 letter words from file
        wordToGuessList = [];

        # opening the text file
        with open(fileName,"rt") as file:

            # reading each line    
            for line in file:

                # reading each word        
                for word in line.split():

                    # store in list
                    wordToGuessList.append(word);
        
        selectRandomWord(wordToGuessList);
    
        
    def selectRandomWord(self):
        #generate a random word from word list
        wordToGuess = random.choice(wordToGuessList);

        #pass the random word to be guessed
        
