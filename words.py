import sys
from Guess import Guess 
from StringDatabase import StringDatabase


def main():
    if len(sys.argv) != 2:
        print("Please use the following format: python3 words.py [play/test]")
        sys.exit(1)

    mode = sys.argv[1].strip().lower()

    if mode not in ["play", "test"]:
        print("Invalid mode. Please use 'play' or 'test'.")
        sys.exit(1)

    wordDatabase = StringDatabase("four_letters.txt")
    guessGame = Guess()
    guessGame.playGame(wordDatabase, mode)


if __name__ == "__main__":
    main()

