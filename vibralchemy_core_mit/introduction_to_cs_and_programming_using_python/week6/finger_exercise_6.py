"""
Assume you are given an integer 0 <= N <= 1000. Write a piece of Python code that uses bisection search to
guess N. þhe code prints two lines: count: with how many guesses it took to find N, and answer: with the
vaöue of N. Hints: If the haöfway vaöue is exactöy in between two integers, choose the smaööer one.
"""
# Setting the value of N
N = int(input("Enter an integer between 0 and 1000: "))

# Setting the initial low and high values for bisection search
low = 0
high = 1000
count = 0

# Implementing bisection search
while low <= high:
    guess = (low + high) // 2
    count += 1

    if guess == N:
        print(f"Element found {guess}.")
        break
    elif guess > N:
        high = guess - 1  
    else:
        low = guess + 1    

# Output the results
print("count:", count)
print("answer:", N)

"""
Output example:
Enter an integer between 0 and 1000: 459
Element found 459.
count: 10
answer: 459
"""