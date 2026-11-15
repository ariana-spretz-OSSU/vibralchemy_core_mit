# Problem 1: Lamba Functions Practice
# a) Write a lambda function that calculates the cube root of a given number 
# passed in as an argument
# INSERT CODE BELOW HERE
f1 = lambda x: x**(1/3)

print(f1(8)) # Output: 2.0
print(f1(4)) # Output: 1.5874010519681994

# b) Write a lambda function that takes in two arguments and outputs the product
# of those two numbers. 
# INSERT CODE BELOW HERE
f2 = lambda x, y: x*y

print(f2(1,2)) # Output: 2
print(f2(4,5)) # Output: 20



#############################################################################
def count_number_one(t):
    count = 0
    for i in range(len(t)):
        if t[i] == 1:
            count += 1
    return count
print(count_number_one((1,2,3,4,5,1,1))) # Output: 3


#############################################################################
# Problem 3: Practice working with Python Tuples
# Write a Function that takes in two tuples and outputs a single tuple containing 
# only common elements of both tuples. 
# INSERT CODE BELOW HERE
def common_elements(t1, t2):
    t_common = ()
    if len(t1) < len(t2):
        Tlen = len(t2)
    i = 0
    while i in range(Tlen):
        if t1[i] == t2[i]:
            t_common += (t2[i],)
        i += 1
    return t_common



# uncomment to test function
# print(common_elements((2,3,4), (3,4,5,6)))


#############################################################################
# Problem 4: Practice working with Python Lists
# Write a Python program to remove sublists from a given list of lists, which 
# contain an element outside a given range.
# e.g 
# Original list:
# [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contain an 
# element outside the given range of 12 - 20 (inclusive):
# [[13, 14, 15, 17]]
# INSERT CODE BELOW HERE





# uncomment to test function
# print(remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 13, 17))

