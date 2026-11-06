############## YOU TRY IT ###############
# Write a program that: 
# * Asks the user for a verb.
# * Prints "I can _ better than you" where you replace _ with the verb.
# * Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run
# your code here

verb = input("Enter a verb: ")
print(f"I can {verb} better than you.")
print((verb + " ") * 4 + verb)
"""
Output:
Enter a verb: cook
I can cook better than you.
cook cook cook cook cook
"""
#########################################

############## YOU TRY IT ###############
# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints a bool depending on whether the guess matches the secret.
# your code here
#########################################
secret = 198
guess = int(input("Enter enter a number between 0 and 500: "))
if guess == secret:
    print(True)
else:
    print(False)

"""
Output:
Enter your guess: 18
False
"""
############## YOU TRY IT ###############
# # Buggy, fix it!
x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: "))
if x == y:
    print(x,"is the same as",y)
else:
    print(x,"is not the same as",y)

"""Output:
Enter a number for x: 98
Enter a different number for y: 56
98 is not the same as 56
"""
#########################################

############## YOU TRY IT ###############
# What's printed when y = 2, y = 20, y = 11?
# What if "if x <= y:" becomes "elif x <= y:"
# answer = ''
# x = 11
# y = 2 # try 20 and 11
# if x == y:
#     answer = answer + 'M'
# if x <= y:   # try making this line: elif x <= y:
#     answer = answer + 'i'
# else:
#     answer = answer + 'T'
# print(answer)
# Output: t

answer = ''
x = 11
y = 2 # try 20 and 11
if x == y:
    answer = answer + 'M'
elif x <= y:   # try making this line: elif x <= y:
    answer = answer + 'i'
else:
    answer = answer + 'T'
print(answer)

# Output: t

answer = ''
x = 11
y = 20 # try 20 and 11
if x == y:
    answer = answer + 'M'
if x <= y:   # try making this line: elif x <= y:
    answer = answer + 'i'
else:
    answer = answer + 'T'
print(answer)

# Output: i

answer = ''
x = 11
y = 20 # try 20 and 11
if x == y:
    answer = answer + 'M'
elif x <= y:   # try making this line: elif x <= y:
    answer = answer + 'i'
else:
    answer = answer + 'T'
print(answer)

# Output: i

answer = ''
x = 11
y = 11 # try 20 and 11
if x == y:
    answer = answer + 'M'
if x <= y:   # try making this line: elif x <= y:
    answer = answer + 'i'
else:
    answer = answer + 'T'
print(answer)

# Output: Mi

answer = ''
x = 11
y = 11 # try 20 and 11
if x == y:
    answer = answer + 'M'
elif x <= y:   # try making this line: elif x <= y:
    answer = answer + 'i'
else:
    answer = answer + 'T'
print(answer)

# Output: Mi
#########################################

############## YOU TRY IT ###############
# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints whether the guess is too low, too high, or the same as the secret. 
# your code here
secret = 198
guess = int(input("Enter enter a number between 0 and 500: "))
if guess < secret:
    print(f"{guess} is too low.")
elif guess > secret:
    print(f"{guess} is too high.")
else:
    print(f"{guess} is the same as the secret number.")

"""
Output:
Enter your guess: 24
24 is too low.
"""
#############################################

#########################################
############### AT HOME ###################
#########################################
# Practice 1: What is the value of s1 and s2?
s1 = "a" + "b"
# Output: ab

d = "hi"
e = " ana"
s2 = d + 2*e
# Output: hi ana ana

# Practice 2: What are the substrings of s?
s = "ABC d3f ghi"
s[0:3:1]
# Output: ABC

s[0:4]
# Output: ABC 

s[8:len(s):3]
# Output: g

s[2::-1]
# Output: CBA

# Practice 3: What does this print?
# Note that a += b is the same as a = a + b
# answer = ''
# x = 11
# # try with y = 2 and y = 12
# y = 2
# if len(str(x)) == len(str(y)):
#     if y != 0 and x%2 == 1:
#         answer = answer + "x / y is " + str(x/y)
# elif x < y:
#     answer += "\nx is smaller"  # \n inserts a newline character in the string
# else:
#     answer += "\ny is smaller"
# print(answer)

# Output: 
#
# y is smaller

answer = ''
x = 11
# try with y = 2 and y = 12
y = 12
if len(str(x)) == len(str(y)):
    if y != 0 and x%2 == 1:
        answer = answer + "x / y is " + str(x/y)
elif x < y:
    answer += "\nx is smaller"  # \n inserts a newline character in the string
else:
    answer += "\ny is smaller"
print(answer)

# Output: x / y is 0.9166666666666666

# Practice 4: Uncomment the code below and:
# if ( a == int(b) ):
#     print("int conversion")
# if ( a == int(b) ) and ( str(a) == b ):
#     print("int and str conversion")
# else: 
#     print("interesting")

# What does it print when a = 6 and b = "6"
"""
Output:
int conversion
int and str conversion
"""
# What does it print when a = "1" and b = 1
"""
Output:
interesting
"""
# What does it print when a = 3 and b = 3
"""
Output:
int conversion
interesting
"""
# What does it print when a = "1" and b = "1"
"""
Output:
interesting
"""
#########################################
############### END AT HOME ##########################
#########################################

