# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

x = float(input("Using bisection search calculate the forth root of: " ))
epsilon = 0.01
ans = x
low = 0
high = ans
# your code here
guess = (high + low)/2
while abs(guess**4 - ans) >= epsilon:
    print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
    if guess**4 < ans:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
print(f'{str(guess)} is close to forth root of {str(ans)}')
"""
Output:
Using bisection search calculate the forth root of: 40
low = 0 high = 40.0 guess = 20.0
low = 0 high = 20.0 guess = 10.0
low = 0 high = 10.0 guess = 5.0
low = 0 high = 5.0 guess = 2.5
low = 2.5 high = 5.0 guess = 3.75
low = 2.5 high = 3.75 guess = 3.125
low = 2.5 high = 3.125 guess = 2.8125
low = 2.5 high = 2.8125 guess = 2.65625
low = 2.5 high = 2.65625 guess = 2.578125
low = 2.5 high = 2.578125 guess = 2.5390625
low = 2.5 high = 2.5390625 guess = 2.51953125
low = 2.5 high = 2.51953125 guess = 2.509765625
low = 2.509765625 high = 2.51953125 guess = 2.5146484375
low = 2.5146484375 high = 2.51953125 guess = 2.51708984375
low = 2.5146484375 high = 2.51708984375 guess = 2.515869140625
low = 2.5146484375 high = 2.515869140625 guess = 2.5152587890625
2.51495361328125 is close to forth root of 40.0
"""

# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range. 
def is_number_in_range(n, start, end):
    if n >= start and n <= end:
        return True
    else:
        return False
    
is_number_in_range(5, 1, 10) 
# output: True
is_number_in_range(15, 1, 10) 
# output: False

# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).
def is_perfect_number(n):
    sum = 0
    for possible_divisor in range(1, n - 1):
        if n % possible_divisor == 0:
            sum += possible_divisor
    if sum == n:
        return True
    else:
        return False
is_perfect_number(6)
is_perfect_number(36)
"""
Output:
True
False
"""

# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

x = float(input("Using approximation algorithm to calculate the forth root of: " ))
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.001
while abs(guess**4 - x) >= epsilon and guess**4 <= x:
    guess += increment
    num_guesses += 1

if abs(guess**4 - x) >= epsilon:
    print('Failed on forth root of', x)
else:
    print(guess, 'is close to forth root of', x)

print('num_guesses =', num_guesses)

"""
Output:
Using approximation algorithm to calculate the forth root of: 16
1.9999999999998905 is close to forth root of 16.0
"""
