""" 
Assume you are given a positive integer variable named N. Write a piece of Python code that prints hello
world on separate lines, N times. You can use either a while loop or a for loop.
"""
# Setting input variables
N = int(input("Enter a positive number: "))
"""
# using a for loop
for i in range(N):
    print("Hello World.") 
"""
# or this one using a while loop
while N > 0:
    print("Hello World.")
    N -= 1

"""
Output example:
Enter a positive number: 5
Hello World.
Hello World.
Hello World.
Hello World.
Hello World.
"""