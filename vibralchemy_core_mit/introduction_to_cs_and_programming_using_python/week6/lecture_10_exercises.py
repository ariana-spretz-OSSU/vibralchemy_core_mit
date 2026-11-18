############# YOU TRY IT #####################
# What is the value of L1, L2, L3, and L after these commands?
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2 # Output: ['re', 'mi']
L3.append(L4) # Output: ['do', ['re', 'mi']]
L = L2.append(L3) # Output: None
#################################################
############### YOU TRY IT #######################
# Write a function that meets the specification:
def make_ordered_list(n):
    """ n is a positive int
    Returns a list containing all ints in order
    from 0 to n (inclusive)
    """
    list = []
    for i in range(0, n + 1):
        #list.append(list[i])
        list.append(i)
    return list
print(make_ordered_list(6)) # Output: [0, 1, 2, 3, 4, 5, 6]

#####################################################
############ YOU TRY IT ###############
def remove_elem(L, e):
    """
    L is a list
    Returns a new list with elements in the same order as L
    but without any elements equal to e.
    """
    new_list = []
    for i in L:
        if i != e:
            new_list.append(i)
    return new_list

L = [1,2,2,2]
print(remove_elem(L, 2)) # Output: [1]
L = [1,2,2,2]
print(remove_elem(L, 1)) # Output: [2,2,2]
L = [1,2,2,2]
print(remove_elem(L, 0)) # Output: [1,2,2,2]

####### YOU TRY IT ###################
def count_words(sen):
    """ sen is a string representing a sentence
    Returns how many words are in sen (i.e. a word is a
    a sequence of characters between spaces. """
    words = sen.split(" ")
    count = 0
    for i in words:
        count += 1
    return (f'number of words in sentence: {count}')
s = "Hello it's me"
print(count_words(s)) # Output: 3
s = "I just took a DNA test turns out I'm 100% splitting strings"
print(count_words(s)) # Output 12
###########################################

############## YOU TRY IT #################
# Write a function that meets this specification
def sort_words(sen):
    """ sen is a string representing a sentence
    Returns a list containing all the words in sen but
    sorted in alphabetical order. """
    word_list = sen.split(' ')
    print(word_list)
    word_list.sort()
    return word_list
s = "look at this photograph"
print(sort_words(s)) # Output: ['at', 'look', 'photograph', 'this']
s = "now this is a story all about how my life got flipped turned upside down"
print(sort_words(s)) # Output: ['a', 'about', 'all', 'down', 'flipped', 'got', 'how', 'is', 'life', 'my', 'now', 'story', 'this', 'turned', 'upside']
##########################################

#######################################
############ AT HOME ###############
#######################################
## Question 1
# What's the value of L3 here?
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
print(L4) # Output: ['re', 'mi']
L3.extend(L4)
print(L3) # Output: ['do', 're', 'mi']
L3.sort()
print(L3) # Output: ['do', 'mi', 're']
del(L3[0])
print(L3) # Output: ['mi', 're']
L3.append(['fa', 'la'])
print(L3) # Output: ['mi', 're', ['fa', 'la']]

## Question 2
# What's the value of brunch here?
L1 = ['bacon', 'eggs']
L2 = ['toast', 'jam']
brunch = L1
print(brunch) # Output: ['bacon', 'eggs']
L1.append('juice')
print(L1) # Output: ['bacon', 'eggs', 'juice']
brunch.extend(L2)
print(brunch) # Output: ['bacon', 'eggs', 'juice', 'toast', 'jam']

## Question 3.
def apply_to_each(L, f):
    """ L is a list of numbers
    f is a list that takes in a number and returns a number
    Mutate L such that you apply function f to every element in L """
    for i in range(len(L)):
        L[i] = f(L[i])
    
test = [1,-2,3]
apply_to_each(test, lambda x: x**2)
print(test) # Output: [1,4,9]
test = [-7, 8, 5, -8, -3]
apply_to_each(test, abs)
print(test) # Output: [7, 8, 5, 8, 3]


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    total_score = (guesses_remaining +4×number of unique letters in secret_word) + (3 × length of secret_word)
    len_secret_word = len(secret_word)
    separator = '----------'
    count_guesses = 10
    vowels = 'aeiou'
    letter_guessed = ''
    print(separator, 'Welcome to Hangman!', separator)
    print('I am thinking of a word that is {len_secret_word} letters long.', separator)
    print('You have {count_guesses} guesses left.')
    print(get_available_letters(letters_guessed))
    guess = input('Please guess a letter: ')
    print(guess)
    if guess.isalpha():
       guess.tolower() 
       if guess in secret_word:
          letter_guessed += guess 
          print('Good guess:', get_word_progress(secret_word, letters_guessed))     
       elif guess in letter_guessed:
            print('Oops! You've already guessed that letter:', get_word_progress(secret_word, letters_guessed))           
       else:
           print('Oops! That letter is not in my word:', get_word_progress(secret_word, letters_guessed))
           count_guesses -= 1
    
       
    elif guess == '!':
        letter_to_reveal(get_available_letters(letters_guessed))
        letter_guessed += revealed_letter
        print('Letter revealed:', revealed_letter,get_word_progress(secret_word, letters_guessed)):
        count_guesses -= 3
        if count_guesses <= 3:
            print('You have currently {count_guesses} guesses left.')
        if count_guesses == 1:
            print('Oops! Not enough guesses left:', get_word_progress(secret_word, letters_guessed)) 

    else:
        print('Oops! That is not a valid letter. Please input a letter from
    the alphabet:', get_word_progress(secret_word, letters_guessed))
    if guess is not in vowels and guess is not in letter_guessed and guess is not in secret_word:
        count_guesses -= 1
    elif guess in vowels and guess is not in letter_guessed and guess is not in secret_word:
        count_guesses -= 2
    elif guess in vowels and guess is not in letter_guessed and guess is not in secret_word:
        if count_guesses == 1:
            print('Game Over')
        
     if has_player_won(secret_word, letters_guessed) == True:
         print('Congratulations, you won!')
     elif count_guesses == 0:
         print('Sorry, you ran out of guesses. The word was', secret_word)
         print('Your total score for this game is:', score)
    
def letter_to_reveal(get_available_letters(letters_guessed)):
    choose_from = ''
    if letter in avaliable_letters and letter in secret_word:
        if letter not in choose_from:
        choose_from += letter
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter




"""
controlar los print y reemplazar por f
"""


    """