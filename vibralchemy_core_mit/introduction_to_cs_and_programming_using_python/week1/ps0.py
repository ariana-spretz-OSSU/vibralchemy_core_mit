""" MIT 6.100L - Problem Set 0 Section 4.3.1: 
Assignment:  
Raising a number to a power and taking a logarithm.
Write a program that does the following in order: 
1. Asks the user to enter a number “x” 
2. Asks the user to enter a number “y”  
3. Prints out number “x”, raised to the power “y”. 
4. Prints out the log (base 2) of “x”.  
"""

import numpy as np

# Setting input variables
x = int(input("Please, enter a number: "))
y = int(input("Please, enter a number: "))

# Mathematical operations
z = x**y

# Output results to the console
print(z)
k = np.log2(x)
print(k)

''' 
Output example:
Please, enter a number: 5
Please, enter a number: 6
15625
2.321928094887362
'''