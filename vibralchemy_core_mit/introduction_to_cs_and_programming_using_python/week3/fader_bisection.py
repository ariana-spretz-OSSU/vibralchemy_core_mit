"""
Implement a manual bisection search algorithm to guess an exact decimal fader factor between 0.0 and 1.0.
Encapsulate the logic into very small functions that adhere to "Clean Code's" rules.
"""
def fader_factor():
    fader = float(input("Enter a fader value between 0.0 and 1.0: "))
    epsilon = 0.0001
    low = 0.0
    high = 1.0
    mid = (low + high) / 2
    while abs(mid - fader) >= epsilon:
        if fader < mid:
            high = mid
            mid = (low + high) / 2
        else:
            low = mid         
            mid = (low + high) / 2

    return (f'{str(mid)} is close to fader factor of {str(fader)}')
fader_factor()
