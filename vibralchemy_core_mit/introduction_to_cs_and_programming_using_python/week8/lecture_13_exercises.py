#########################################
########### YOU TRY IT ##################
##########################################
def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of 
        equal lengths containing numbers
    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 
    Raise a ValueError if Ldenom contains 0. """
    # your code here
    # challenge: write this with list comprehension!
    assert len(Lnum) != 0 and len(Ldenom) != 0, 'no grades data'
    assert len(Lnum) == len(Ldenom), 'list no equal length are given'
    if 0 in Ldenom:
        raise ValueError
    result = [Lnum[i] / Ldenom[i] for i in range(len(Lnum))]  
    return result
    
# For example:
L1 = [4,5,6]
L2 = [1,2,3]    
print(pairwise_div(L1, L2))  # Output: [4.0,2.5,2.0]
L1 = [4,5,6]
L2 = [1,0,3]    
print(pairwise_div(L1, L2))  # raises a ValueError
## to run after introducing assertions
L1 = [4,5,6,7,8]
L2 = [1,8,3]    
print(pairwise_div(L1, L2))  # raises an AssertionError
L1 = []
L2 = []    
print(pairwise_div(L1, L2))  # raises an AssertionError
#########################################

##############################################
################### AT HOME ###################
################################################
def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of equal lengths
        containing numbers
    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 
    Raise a ValueError if L2 contains 0 or if the code can't 
    perform the division for some reason. """
    new_list = []
    assert len(Lnum) != 0 and len(Ldenom) != 0, 'no grades data'
    assert len(Lnum) == len(Ldenom), 'list no equal length are given'
    for i in range(len(Lnum)):
        try:
            result = Lnum[i] / Ldenom[i]
            new_list.extend([result])
        except (ZeroDivisionError, TypeError):
            print('You cannot divide by zero.')
            print('Error in data types.')
            raise ValueError
    return new_list
    
# For example:
L1 = [4,5,6]
L2 = [1,2,3]    
print(pairwise_div(L1, L2))  # Output: [4.0,2.5,2.0]
L1 = [4,5,6]
L2 = [1,0,3]    
print(pairwise_div(L1, L2))  # raises a ValueError
## to run after introducing assertions
L1 = [4,5,6,7,8]
L2 = [1,8,3]    
print(pairwise_div(L1, L2))  # raises an AssertionError
L1 = []
L2 = []    
print(pairwise_div(L1, L2))  # raises an AssertionError