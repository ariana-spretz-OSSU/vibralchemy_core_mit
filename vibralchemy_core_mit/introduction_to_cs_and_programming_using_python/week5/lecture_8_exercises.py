############### YOU TRY IT #######################
# What does this print to the console? 
# Think first, then run it. 
def add(x,y):
    return x+y
def mult(x,y):
    print(x*y)

# add(1,2)
# Output: 3

# print(add(2,3))
# Output: 5

# mult(3,4)
# Output: 12

# print(mult(4,5))
# Output: 20

##################################################
############ YOU TRY IT ####################
# Fix this buggy code so it works according to the specification:
def is_triangular(n):
    """ n is an int > 0 
        Returns True if n is triangular, i.e. equals a continued
        summation of natural numbers (1+2+3+...+k) 
    """
    total = 0
    for i in range(n + 1):
        total += i
        if total == n:
            return True
    return False
print(is_triangular(4))  
# Output: False

print(is_triangular(6))  
# Output: True

print(is_triangular(1))  
# Output: True
            
# # start by runing it on simple test cases
# print(is_triangular(4))  # print False
# print(is_triangular(6))  # print True
# print(is_triangular(1))  # print True
##############################################

###################### YOU TRY IT ######################
def count_nums_with_sqrt_close_to(n, epsilon):
    """ n is an int > 2
        epsilon is a positive number < 1
    Returns how many integers have a square root within epsilon of n """
    # your code here
#print(count_nums_with_sqrt_close_to(10, 0.1))
#############################################################

############## YOU TRY IT ###############
def apply(criteria,n):
    """ criteria is a function that takes in a number and returns a Boolean
        n is an int
    Returns how many ints from 0 to n (inclusive) match the criteria 
    (i.e. return True when criteria is applied to them)
    """ 
    # your code here
def is_even(x):
    sum_int = 0
    return x%2==0
how_many = apply(is_even,10)
# print(how_many)


############## YOU TRY IT ###############
# Write a function that takes in an int and two functions as 
# parameters (each takes in an int and returns a float). 
# It applies both functions to numbers between 0 and n (inclusive) 
# and returns the maximum value of all outcomes. 
def max_of_both(n, f1, f2):
    """ n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    Returns the maximum value of all these results.
    """
    # your code here
# print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
# print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20
################################

###################################
############# AT HOME #######################
###################################
def is_palindrome(s):
    """ s is a string
    Returns True if s is a palnidrome and False otherwise. 
    A palindrome is a string that contains the same 
    sequence of characters forward and backward """
    # your code here
    for char in range(len(s)):
        reverse = s[::-1]
        if s[char] == reverse[char]:
            return True
        else:
            return False

print(is_palindrome("222"))
# Output: True
print(is_palindrome("2222"))   
# Output: True
print(is_palindrome("abc"))  
# Output: False

def f_yields_palindrome(n, f):
    """ n is a positive int
        f is a function that takes in an int and returns an int
    Returns True if applying f on n returns a number that is a
    palindrome and False otherwise.  """
    # your code here
# For example:
def f(x):
    return x+1
def g(x):
    return x*2
def h(x):
    return x//2
# print(f_yields_palindrome(2, f))   # prints True
# print(f_yields_palindrome(76, f))   # prints True
# print(f_yields_palindrome(11, g))   # prints True
# print(f_yields_palindrome(123, h))   # prints False
    
###################################
##################################
###################################



