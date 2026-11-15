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
    sum = 0
    prod = 1
    for i in range(len(L)):
        print(i)
        sum += L[i] 
        print(L[i])
        print(sum)
        prod *= L[i] 
        print(L[i])
        print(prod)
    return (sum, prod)
        
print(sum_and_prod([4,6,2,5]))   # Output: (17, 240)

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

always_sunny(('cloudy' ), ('cold',))  # Output: ('sunny', 'ccold')

def max_of_both(n, f1, f2):
    """ n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    Returns the maximum value of all these results.
    """
    max = 0
    for i in range(0, n + 1):
        if f1(i) > max:
            max = f1(i)
            print("max is:", max)
        if f2(i) > max:
            max = f2(i)
            print("max is:", max)
    return max

print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # Output: 3
print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # Output: 20


def sublist_sum(L):
    """ L is a list whose elements are lists with int elements
    Returns the sum of all int elements. """
    # your code here
    sum = 0
    for i in range(len(L)):
        for n in range(len(L[i])):
            sum += L[i][n]
    
    return sum

print(sublist_sum([[1,2], [4,5,6]])) # Output: 18