# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    letters_not_guessed = ''
    for letter in secret_word:
        if letter not in letters_guessed:
            letters_not_guessed += '*'
        else:
            letters_not_guessed += letter
            
    return letters_not_guessed


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    letters_not_yet_guessed = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            letters_not_yet_guessed += letter
    return letters_not_yet_guessed


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    len_secret_word = len(secret_word)
    separator = '---------------'
    count_guesses = 10
    vowels = 'aeiou'
    letters_guessed = []
    i = 0
    with_help = False
    
    print(separator, 'Welcome to Hangman!', separator)
    print('I am thinking of a word that is', len_secret_word,'letters long.')
    print(separator * 4)

    while count_guesses >= 0: 
        guess = input('Please guess a letter: ') 
        print('You have', count_guesses, 'guesses left.')
        print(get_available_letters(letters_guessed)) 
        print(separator * 4) 
        if guess.isalpha():
            guess.lower() 
            if guess in secret_word and guess not in letters_guessed:
                letters_guessed.extend(guess) 
                print('Good guess:', get_word_progress(secret_word, letters_guessed))  
                print(separator * 4)
            elif guess in secret_word and guess in letters_guessed:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed)) 
                print(separator * 4)                      
            
            if guess not in vowels and guess not in letters_guessed and guess not in secret_word:
                print('Oops! That letter is not in my word:', get_word_progress(secret_word, letters_guessed))
                print(separator * 4)
                count_guesses -= 1
            elif guess in vowels and guess not in letters_guessed and guess not in secret_word:
                print('Oops! That letter is not in my word:', get_word_progress(secret_word, letters_guessed))
                print(separator * 4)
                count_guesses -= 2
            
            if count_guesses == 0:
                print(separator * 4) 
                print('Sorry, you ran out of guesses. The word was', secret_word)
                print('Game Over!')   
                print(separator * 4)         
                break
            if len(secret_word) == len(letters_guessed):
                print(separator * 4) 
                print('Congratulations, you won!')
                print('Your total score for this game is:', score)
                print(separator * 4)
                break
                     
        elif guess == '!':
            revealed_letter = letter_to_reveal(get_available_letters(letters_guessed))
            letters_guessed += revealed_letter
            print('Letter revealed:', revealed_letter, get_word_progress(secret_word, letters_guessed))
            count_guesses -= 3
            if count_guesses <= 3:
                print('You have currently', count_guesses, 'guesses left.')
            if count_guesses == 1:
                print('Oops! Not enough guesses left:', get_word_progress(secret_word, letters_guessed)) 
                print(separator * 4) 
        else:
            print('Oops! That is not a valid letter. Please input a letter from the alphabet:', get_word_progress(secret_word, letters_guessed))
            print(separator * 4) 
             
        i += 1     
            

def letter_to_reveal(secret_word, letters_guessed):
    choose_from = ''
    if letter in letters_guessed and letter in secret_word:
        if letter not in choose_from:
          choose_from += letter
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter

def score(word, number_of_guesses):
    total_score = (guesses_remaining + (4 * number_of_unique_letters in secret_word) + (3 * len_secret_word))
    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

