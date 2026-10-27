"""
Assume you are given a variable named number (has a numerical value). Write a piece of python code that prints out one of the following strings:
positive if the variable number is positive,
negative if the variable number is negative,
zero if the variable number is equal to zero.
"""
# Setting input variables
number = int(input("type a number: "))
answer = "The number you have chosen is:"

# Determine if the number is positive, negative, or zero
if number > 0:
     print(answer, "positive")
elif number < 0:
     print(answer, "negative")
else:     
     print(answer, "zero")

""" 
Output example:
type a number: 19
The number you have choosed is: positive
"""
