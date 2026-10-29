####################################################################################
# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

# Insert code below

name = input("Enter your name: ")
l = len(name) - 5
print("The length of your name minus 5 is:", l)

""" Enter your name: Ariana
The length of your name minus 5 is: 1 """

####################################################################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.

test_string = "We want to remove the nth character from this string"
n = 8

# Insert code below
new_string = test_string[:n] + test_string[n+1:]
print("Old string:", test_string)
print("New string:", new_string)



####################################################################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.

my_string = "This is my string"  # example string - modify to test

# Insert code below
if len(my_string) > 10 or len(my_string) < 5:
    print("True")
else:
    print("False")
    
# True


####################################################################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string

my_string = "How many times is the letter e in this string?"

# Insert code below

E = "e"
count = 0
for i in my_string:
    if i == E:
        count += 1
        
print("The number of 'e's in the string is:", count)



