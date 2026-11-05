"""
Assume you are given a positive integer variable named N. Write a piece of Python code that finds the cube
root of N. The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. Hint:
use a loop that increments a counter -- you decide when the counter should stop.
"""

N = int(input("Enter a positive number: "))
counter = 0
while counter ** 3 < N:
    counter += 1
if counter ** 3 == N:
    print(counter)
else:
    print("error")

"""
Output example:
Enter a positive number: 27
3
"""