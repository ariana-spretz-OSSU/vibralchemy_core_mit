#################################################
######################## AT HOME ##########################
#################################################
# 1. If you are incrementing from 0 by 0.022, how many increments 
# can you do before you get a floating point error? 
# x = 0
# count = 20     # check different numbers here
# for i in range(count):
#     x += 0.022 # increment
#     print(x)      # check this value for floating point error
# your code here
"""
Output:
0.022
0.044
0.066
0.088
0.10999999999999999
0.13199999999999998
0.15399999999999997
0.17599999999999996
0.19799999999999995
0.21999999999999995
0.24199999999999994
0.26399999999999996
0.286
0.308
0.33
0.35200000000000004
0.37400000000000005
0.3960000000000001
0.4180000000000001
0.4400000000000001

# count = 5
0.022
0.044
0.066
0.088
0.10999999999999999

"""
# 2. Automate the code from the previous problem. Suppose you are 
# just given an increment value. Write code that automatically
# determines how many times you can add increment to itself 
# until you start to get a floating point error.
# your code here
x = 0
count = 20 
add = str(0.022)
increment = 0.022
len_increment = len(add)
floating_point = add.find(".")
N = len_increment - floating_point - 1
for i in range(count):
    x += increment 
    formated_value = f"{x:.{N}f}"
    if str(x) != formated_value:
        break
print(f"Number of times until you start to get a floating point error: { i + 1 }")

"""
Output:
Number of times until you start to get a floating point error: 5
"""
#################################################
#################################################
#################################################

