"""
Implement a manual bisection search algorithm to guess an exact decimal fader factor between 0.0 and 1.0.
Encapsulate the logic into very small functions that adhere to "Clean Code's" rules.
"""
def fader_input():
    fader = float(input("Enter a fader value between 0.0 and 1.0: "))
    return fader

def close_fader_value(mid, fader, epsilon):
    if abs(mid - fader) <= epsilon:
        return True
    else:
        return False

def calc_mid_point(low, high):
    mid = (low + high) / 2
    return mid

def bisection_search_fader(close_fader_value, calc_mid_point, fader, epsilon):
    low = 0.0
    high = 1.0
    mid = calc_mid_point(low, high)
    while not close_fader_value(mid, fader, epsilon):
        if fader < mid:
            high = mid
            mid = calc_mid_point(low, high)
        else:
            low = mid
            mid = calc_mid_point(low, high)
    return mid
    
def print_final_output(mid, fader):
    return (f'{str(mid)} is close to fader factor of {str(fader)}')

def fader_factor():
    fader = fader_input()
    epsilon = 0.0001
    result_mid = bisection_search_fader(close_fader_value, calc_mid_point, fader, epsilon)
    return print_final_output(result_mid, fader)
    
fader_factor()

