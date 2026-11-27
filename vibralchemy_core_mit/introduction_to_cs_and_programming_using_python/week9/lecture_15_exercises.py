############### YOU TRY IT #################
# Calculate n**p recursively by writing this function
def power_recur(n, p):
    if p == 0 :
        return 1
    elif p == 1 :
        return n
    else:
        return n * power_recur(n, p - 1)
        
print(power_recur(2,3))  # Output: 8

################################################

#######################################################
################ AT HOME ##############################
#######################################################
# Q1. Rewrite this to calculate b+b+b... a times
def mult(a, b):
    if a == 1:
        return b
    else:
        return b + mult(a - 1, b)
    
print(mult(5,4)) # Output: 20

# Q2. If we evaluate mult_recur(3,4), how many times is the 
# procedure mult_recur called (including initial call)?
# Hint: add a print inside the function!

def mult_recur(a,b):
    if b == 0:
        return 0
    else:
        return a + mult_recur(a,b-1)

mult_recur(3,4)
"""
Output:
Call #1 (a=3, b=4)
Call #2 (a=3, b=3)
Call #3 (a=3, b=2)
Call #4 (a=3, b=1)
Call #5 (a=3, b=0)
"""

# Q3. Calculate a+b recursively. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add(a, b):
    if b == 0:
        return a
    else:
        return 1 + add(a, b - 1)

print(add(3, 4))  # Output: 7


# Q4. Calculate a+b recursively by 1's. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add_by_ones(a, b):
    """ Uses recursion to calculate a+b as adding
    1, a times then adding 1, b times. """
    if b == 0:
        return a
    else:
        return add_by_ones(a + 1, b - 1)

print(add_by_ones(3,4)) # Output: 7

