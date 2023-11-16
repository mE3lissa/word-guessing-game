#very simply non object oriented file. It simply parses the command line parameter and starts the guessing game.

import sys  # to parse the command line parameter
import Guess;
import Game;
import StringDatabase;


def main():
    if "play" in sys.argv:
        
        # start the guess
        print("play now");
        
    elif "test" in sys.argv:
        
        # start the test
        print("test now");



# run main if this file is main 
if __name__ == "__main__":
    main();



#run all files
#python3 words.py test (words.py is the driver)