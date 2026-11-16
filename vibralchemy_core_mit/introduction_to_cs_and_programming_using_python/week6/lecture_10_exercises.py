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
