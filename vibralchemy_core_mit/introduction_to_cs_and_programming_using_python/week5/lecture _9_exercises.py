############### YOU TRY IT #####################
# Write a function that meets these specifications:
def char_counts(s):
    """ s is a string of lowercase chars 
    Returns a tuple where the first value is the 
    number of vowels in s and the second value 
    is the number of consonants in s 
    """
    # your code here
    letters = 'aeiou'
    vowels = 0
    consonants = 0
    i = 0
    
    while i in range(len(s)):
        char = s[i]
        if char in letters:
            vowels += 1
        else:
            consonants += 1
        i += 1
    return (vowels, consonants)
    

print(char_counts("abcd"))  # Output: (1,3)
print(char_counts("zcght"))  # Output: (0,5)

##################################################

################## YOU TRY IT ###################
def sum_and_prod(L):
    """ L is a list of numbers 
    Return a tuple where the first value is the 
    sum of all elements in L and the second value 
    is the product of all elements in L 
    """
    # your code here

 

# print(sum_and_prod([4,6,2,5]))   # prints (17, 240)

#############################################
################## AT HOME ####################
#############################################

# Trace this code:
# Figure out what it returns and then run it to check yourself.
def always_sunny(t1, t2):
    """ t1, t2 are non-empty """
    sun = ("sunny", "sun")
    first = t1[0] + t2[0]
    return (sun[0], first)

# always_sunny(('cloudy' ), ('cold',))  # returns what?



def max_of_both(n, f1, f2):
    """ n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    Returns the maximum value of all these results.
    """
    # your code here

# print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
# print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20


def sublist_sum(L):
    """ L is a list whose elements are lists with int elements
    Returns the sum of all int elements. """
    # your code here

# print(sublist_sum([[1,2], [4,5,6]])) # prints 18