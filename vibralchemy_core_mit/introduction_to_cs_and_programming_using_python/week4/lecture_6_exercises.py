############### YOU TRY IT ###################
# x = 0.5
# epsilon = 0.01
# # choose the low endpoint
# low = ???
# # choose the high endpopint
# high = ???
# guess = (high + low)/2
# while abs(guess**2 - x) >= epsilon:
#     #print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# print(f'{str(guess)} is close to square root of {str(x)}')
#####################################################
x = 0.5
epsilon = 0.01
# choose the low endpoint
low = 0
# choose the high endpopint
high = 1
guess = (high + low)/2
while abs(guess**2 - x) >= epsilon:
    print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
print(f'{str(guess)} is close to square root of {str(x)}')

"""OUtput:
low = 0 high = 1 guess = 0.5
low = 0.5 high = 1 guess = 0.75
low = 0.5 high = 0.75 guess = 0.625
low = 0.625 high = 0.75 guess = 0.6875
low = 0.6875 high = 0.75 guess = 0.71875
0.703125 is close to square root of 0.5
"""

################# YOU TRY IT #######################
# Write code to use bisection search to find the cube 
# root of positive cubes to within some epsilon
cube = 27
epsilon = 0.01
low = 0
high = cube
# your code here
guess = (high + low)/2
while abs(guess**3 - cube) >= epsilon:
    print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
print(f'{str(guess)} is close to cube root of {str(cube)}')

"""
Output:
low = 0 high = 27 guess = 13.5
low = 0 high = 13.5 guess = 6.75
low = 0 high = 6.75 guess = 3.375
low = 0 high = 3.375 guess = 1.6875
low = 1.6875 high = 3.375 guess = 2.53125
low = 2.53125 high = 3.375 guess = 2.953125
low = 2.953125 high = 3.375 guess = 3.1640625
low = 2.953125 high = 3.1640625 guess = 3.05859375
low = 2.953125 high = 3.05859375 guess = 3.005859375
low = 2.953125 high = 3.005859375 guess = 2.9794921875
low = 2.9794921875 high = 3.005859375 guess = 2.99267578125
low = 2.99267578125 high = 3.005859375 guess = 2.999267578125
low = 2.999267578125 high = 3.005859375 guess = 3.0025634765625
low = 2.999267578125 high = 3.0025634765625 guess = 3.00091552734375
3.000091552734375 is close to cube root of 27
"""
#####################################################

