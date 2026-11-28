"""
Implement the function that meets the specification below:
"""
def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    if len(L) == 0:
        return []
    elif type(L[0]) == list:
        new_list = flatten(L[0]) + flatten(L[1:])
        return new_list
    else:
        return [L[0]] + flatten(L[1:])

# Examples: 
L = [[1, 4, [6], 2], [[[3]], 2], 4, 5] 
print(flatten(L))  # Output: [1, 4, 6, 2, 3, 2, 4, 5]
