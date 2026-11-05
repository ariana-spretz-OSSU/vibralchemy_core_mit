"""
Assume you are given a string variabe named my_str. Write a piece of Python code that prints out 
a new string containing the even indexed characters of my_str For example, if my_str = "abcdefg" 
your code should print out aceg.
"""

my_str = "abcdefg"
new_string = my_str[::2]
print(new_string)

# Output example
# aceg