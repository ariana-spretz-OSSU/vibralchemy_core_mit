"""
Implement the function that meets the specification below.:
"""
def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic a×x² + b×x + c.
    """
    # Your code here 
    return a * x **2 + b * x + c

eval_quadratic(1, 1, 1, 1) # prints 3
print(eval_quadratic(1, 1, 1, 1))
# Output: 3

# Examples: 
# print(eval_quadratic(1, 1, 1, 1)) # prints 3 