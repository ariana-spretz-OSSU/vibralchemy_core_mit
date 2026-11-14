############ YOU TRY IT ###############
# This one is similar to remove_elem from lec10 except that remove_elem 
# returns a new list and this one mutates the parameter L (and returns None)
def remove_all(L, e):
    """ 
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    # your code here
    

# Lin = [1,2,2,2]
# remove_all(Lin, 2)
# print(Lin)    # prints [1]

# Lin = [1,2,2,2]
# remove_all(Lin, 1)
# print(Lin)    # prints [2, 2, 2]

# Lin = [1,2,2,2]
# remove_all(Lin, 0)
# print(Lin)    # prints [1, 2, 2, 2]

#######################################

############ YOU TRY IT AT HOME ###################
# Step through the code below without running it
# Write down what values each variable has
# Draw the memory diagram to help you keep track of aliases and clones

# cool = ['blue', 'green']
# warm = ['red', 'yellow', 'orange']
# print(cool)
# print(warm)

# colors1 = [cool]
# print(colors1)
# colors1.append(warm)
# print('colors1 = ', colors1)

# colors2 = [['blue', 'green'],
#           ['red', 'yellow', 'orange']]
# print('colors2 =', colors2)

# warm.remove('red') 
# print('colors1 = ', colors1)
# print('colors2 =', colors2)

# for e in colors1:
#     print('e =', e)

# for e in colors1:
#     if type(e) == list:
#         for e1 in e:
#             print(e1)
#     else:
#         print(e)

# flat = cool + warm
# print('flat =', flat)

# print(flat.sort())
# print('flat =', flat)

# new_flat = sorted(flat, reverse = True)
# print('flat =', flat)
# print('new_flat =', new_flat)

# cool[1] = 'black'
# print(cool)
# print(colors1)

###############################




############################################
################### AT HOME ######################
############################################
def repeat(L, n):
    """ L is a list of ints
        n is a positive int
    Mutates L to contain whatever elements L has right now repeated n times. """
    # your code here 
    
# Lin = [1,2,3]
# repeat(Lin, 3)
# print(Lin)    # prints [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Think about why the following solution does not work!
def repeat(L, n):
    """ L is a list of ints
        n is a positive int
    Mutates L to contain whatever elements L has right now repeated n times. """
    # your code here 
    Lnew = []
    for i in range(n):
        for e in L:
            Lnew.append(e)
    Lin = Lnew  # hint, even thought we reuse the name Lin here, we make it point to a NEW object!
    
# Lin = [1,2,3]
# repeat(Lin, 3)
# print(Lin)   # prints [1, 2, 3] which is wrong!


###########################################¤#N######¤#N#

