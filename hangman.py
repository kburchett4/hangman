
import random
import string
from os import system
import sys
from time import sleep

WORDLIST_FILENAME = "~/words.txt"

hang_temp = {10: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
  |   |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
  |   |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |
 /
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      |
=========''', '''
  +---+
  |   |
  X   |
 /|\  |
  |   |
 / \  |
 DEAD |
========='''], 9: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
  |   |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
  |   |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |
 /
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      |
=========''', '''
  +---+
  |   |
  X   |
 /|\  |
  |   |
 / \  |
 DEAD |
========='''], 8: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
  |   |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
  |   |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |
 /
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      |
=========''', '''
  +---+
  |   |
  X   |
 /|\  |
  |   |
 / \  |
 DEAD |
========='''], 7: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
DEAD  |
========='''], 6: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  X   |
 /|\  |
 / \  |
 DEAD |
========='''], 5: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
 DEAD |
========='''], 4: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
 DEAD |
========='''], 3: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

   +---+
   |   |
   X   |
  /|\  |
  / \  |
D E A D|
========='''], 2: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  X   |
 /|\  |
 / \  |
DEAD  |
========='''], 1: ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  X   |
 /|\  |
 / \  |
DEAD  |
=========''']}
def main():
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)

def clear_screen():
    sleep(1)
    system('clear')
    sleep(1)

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    clear_screen()
    print("\n\n\n\nLoading word list from file...\n\n")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# def playAgain(secretWord=None, wordlist=None, main):
#     while True:
#
#         try:
#             round = input("Do you want to play again? y or n ?")
#             if round == 'n':
#                 sys.exit
#
#             if round == 'y':
#                 main()
#
#         except ValueError:
#             print("Sorry, I didn't understand that.",)
#             continue


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
    '''
    count = 0
    for x in secretWord:
        if x not in lettersGuessed:
            count+=1

        if count >= 1:
            return False
        return count
    return True


def guessedLetterCount(secretWord, lettersGuessed):
    right = []
    for x in secretWord:
        if x in lettersGuessed:
            right.append(x)

    z = len(right)
    return z


def getGuessedWord(secretWord, lettersGuessed, correctLetters):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed so far.
    '''
    guessed = ""
    guess = ""

    for char in secretWord:
        if char in lettersGuessed:
             guessed += char
        else:
            guessed += " _ "

    for char in correctLetters:
        if  char in correctLetters:
            guess += char

        else:
            guess += " _ "

    return guessed
    return guess

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list what letters have been guessed so far
    return: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
    available = alpha[:]

    for e in lettersGuessed:
        if e in available:
            available.remove(e)
    return ''.join(available)


def displayBoard(map_hang, guessesLeft, correctLetters, secretWord):
    board = len(secretWord) - guessesLeft

    print(map_hang[board])

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess about
      whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed

    '''

    guessesLeft = len(secretWord)
    map_hang = hang_temp.get(len(secretWord))
    lettersGuessed = []
    correctLetters = []
    clear_screen()


    print("\n\n\n\n\n\n\nWelcome to the game, Hangman!")
    print("\nI am thinking of a word that is", len(secretWord), "letters long.\n")
    print(getGuessedWord(secretWord, lettersGuessed, correctLetters))
    print("\nYou have", (guessesLeft), "guesses left.")


    while not isWordGuessed(secretWord, lettersGuessed) and guessesLeft > 0:
        while True:
            try:
                guess = input("\nPlease guess a letter: ").lower()

                if guess not in string.ascii_lowercase:
                    print("Sorry, only one letter at a time. Try again...")
                    continue
                if len(guess) > 1:
                    print("Thats too many letters, please try again. ")

                if guess == "":
                    print("Sorry, you must enter a letter. Try again. ")
                    continue

                if guess in lettersGuessed:
                    print("\nOops! You've already guessed that letter: " )
                    print('\nAvailable letters:  ', getAvailableLetters(lettersGuessed))
                    print("\n--------")
                    print("\nTry again ... ")
                    continue
                clear_screen()

            except ValueError:
                print("Sorrry, I didn't understand that.")
                continue

            else:
                break

        lettersGuessed += guess

        if isWordGuessed(secretWord, lettersGuessed):
            print("\nGood guess: ", getGuessedWord(secretWord, lettersGuessed, correctLetters))
            clear_screen()
            print("Congratulations! You Won!")
            print("\n*-*-*-*-*-*-*-*-*-*-*-*-*")


            ## TODO: playagain()

            """
            something like
            if playagain:
                    hangman(secretWord)
                else:
                    tally up the total rounds Won with the words guessed and
                    askif they would like to save game data - think classic
                    highscore saves
                        # brings a whole new elment implementing the highscore
                            - user would be instructed to fill out a few inputs
                            then take the data from the running terminal(maybe
                            each round) as well as the data from inputs and
                            upload that to a vm DB holding the winnings of all
                            users for all games(if we implement more games into
                            the py dev/learn games suite)
                    break
                    """
            break

        elif guess in secretWord:
            clear_screen()
            displayBoard(map_hang, guessesLeft, correctLetters, secretWord)
            print("Good Guess: ", getGuessedWord(secretWord, lettersGuessed, correctLetters))
            print('\nAvailable letters:  ', getAvailableLetters(lettersGuessed))
            print("\n------------------------")
            guessesLeft -= 1
            correctLetters.append(guess)
            print("You have", guessesLeft, "guesses left.")
            guessedLetterCount(secretWord, lettersGuessed)
            print("------------------------")

        else:
            guessesLeft -= 1
            clear_screen()
            displayBoard(map_hang, guessesLeft, correctLetters, secretWord)
            print("\nOops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed, correctLetters))
            print('\nAvailable letters:  ', getAvailableLetters(lettersGuessed))
            print("\n------------------------")
            print("You have", guessesLeft, "guesses left.")
            guessedLetterCount(secretWord, lettersGuessed)
            print("------------------------")

        if guessesLeft == 1:
            getGuessedWord(secretWord, lettersGuessed, correctLetters)
            final_guess = input("You have one guess left with more than one tile to fill...please guess the word.")
            if final_guess == secretWord:
                print("Good Guess....")
                clear_screen()
                print("\nCongratulations! You Guessed The Word:  ", secretWord)
                ## TODO: playagain()
                    ## See above explanation
            else:
                guessesLeft -= 1
        if guessesLeft == 0:
            displayBoard(map_hang, guessesLeft, correctLetters, secretWord)
            print("\n\n\nSorry, you ran out of guesses. The word was ", secretWord, "\n\n")
            while True:

                try:
                    round = input("Do you want to play again? y or n ?")
                    if round == 'n':
                        clear_screen()
                        print("\n\n\n\n\n            Thanks for Playing!")
                        sleep(2)
                        print("\n\n\n\n\n            Brought to you by: \n\n       --- Terminally ill Games ---")
                        sleep(5)
                        clear_screen()
                        break

                    if round == 'y':
                        clear_screen()
                        print("Alright....Let's Do This!")
                        clear_screen()
                        main()

                except ValueError:
                    print("Sorry, I didn't understand that.",)
                    continue
            break

if __name__ == '__main__':
    main()


# so that it can be accessed from anywhere in the program
