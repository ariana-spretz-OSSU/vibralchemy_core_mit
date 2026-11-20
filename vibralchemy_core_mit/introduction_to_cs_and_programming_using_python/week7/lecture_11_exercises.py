############ YOU TRY IT ###############
# This one is similar to remove_elem from lec10 except that remove_elem 
# returns a new list and this one mutates the parameter L (and returns None)
def remove_all(L, e):
    """ 
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    for i in L[:]:
        if i == e:
            L.remove(i)
    
Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin)    # prints [1]

Lin = [1,2,2,2]
remove_all(Lin, 1)
print(Lin)    # prints [2, 2, 2]

Lin = [1,2,2,2]
remove_all(Lin, 0)
print(Lin)    # prints [1, 2, 2, 2]

#######################################

############ YOU TRY IT AT HOME ###################
# Step through the code below without running it
# Write down what values each variable has
# Draw the memory diagram to help you keep track of aliases and clones

cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool) # Output: ['blue', 'green']
print(warm) # Output: ['red', 'yellow', 'orange']

colors1 = [cool]
print(colors1) # Output: [['blue', 'green']]
colors1.append(warm)
print('colors1 = ', colors1) # Output: colors1 =  [['blue', 'green'], ['red', 'yellow', 'orange']]

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']]
print('colors2 =', colors2) # Output: colors2 = [['blue', 'green'], ['red', 'yellow', 'orange']]

warm.remove('red') 
print('colors1 = ', colors1) # Output: colors1 =  [['blue', 'green'], ['yellow', 'orange']]
print('colors2 =', colors2) # Output: colors2 = [['blue', 'green'], ['red', 'yellow', 'orange']]

for e in colors1:
    print('e =', e) 
""" 
Output: blue
green
yellow
orange 
"""

for e in colors1:
    if type(e) == list:
        for e1 in e:
            print(e1) # Output: e = ['blue', 'green']
    else:
        print(e) # Output: e = ['yellow', 'orange']

flat = cool + warm
print('flat =', flat) # Output: flat = ['blue', 'green', 'yellow', 'orange']

print(flat.sort()) # Output: None
print('flat =', flat) # Output: flat = ['blue', 'green', 'orange', 'yellow']

new_flat = sorted(flat, reverse = True)
print('flat =', flat) # Output: flat = ['blue', 'green', 'orange', 'yellow']
print('new_flat =', new_flat) # Output: new_flat = ['yellow', 'orange', 'green', 'blue']

cool[1] = 'black'
print(cool) # Output: ['blue', 'black']
print(colors1) # Output: [['blue', 'black'], ['yellow', 'orange']]

###############################


############################################
################### AT HOME ######################
############################################
def repeat(L, n):
    """ L is a list of ints
        n is a positive int
    Mutates L to contain whatever elements L has right now repeated n times. """
    original_len = len(L)
    for j in range(0, n - 1):
        for i in range(0, original_len):
            L.append(L[i])
Lin = [1,2,3]
repeat(Lin, 3)
print(Lin)    # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]


###########################################¤#N######¤#N#

