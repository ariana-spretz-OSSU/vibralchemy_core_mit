################## YOU TRY IT #########################
def find_grades(grades, students):
    """ grades is a dict mapping student names (str) to grades (str)
        students is a list of student names 
    Returns a list containing the grades for students (in the same order) """
    # your code here
  
d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
# print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']

########################################################
################## YOU TRY IT #########################
def find_in_L(Ld, k):
    """ L is a list of dicts
        k is an int
    Returns True if k is a key in any dicts of L and False otherwise """
    # your code here
  
d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
# print(find_in_L([d1, d2, d3], 2))  # returns True
# print(find_in_L([d1, d2, d3], 25))  # returns False
########################################################
########################### YOU TRY IT ######################
def count_matches(d):
    """ d is a dict
    Returns how many entries in d have the key equal to its value """
    # your code here
d = {1:2, 3:4, 5:6}
# print(count_matches(d))   # prints 0
d = {1:2, 'a':'a', 5:5}
# print(count_matches(d))   # prints 2
##############################################################
############# YOU TRY IT ###################
my_d ={'Ana':{'mq':[10], 'ps':[10,10]}, 
       'Fredo':{'ps':[7,8], 'mq':[8]},
       'Eric':{'mq':[3], 'ps':[0]}      }
def get_average(data, what):
    """ data is a dict like my_d above
        what is 'ps' or 'mq'
        Returns the average of all elements in data that match 'what' """
    all_data = []
    for stud in data.keys():
        pass
        # Which one of the below is correct? 
        # A) all_data = all_data + data[stud][what]
        # B) all_data.append(data[stud][what]) 
        # C) all_data = all_data + data[stud[what]]
        # D) all_data.append(data[stud[what]]) 
    return sum(all_data)/len(all_data)
# print(get_average(my_d, 'mq') )   # prints 7.0
###########################################################

######################################################
############## AT HOME ###################
######################################################
def is_inverse(d1, d2):
    """ d1 and d2 are dicts 
    Assume values of d1 and d2 are unique and immutable
    Returns True if d1's keys are values in d2 and d1's 
    values are keys in d2 """
    pass
# d1 = {1:2, 3:4}
# d2 = {2:1, 4:3}
# print(is_inverse(d1, d2))  # prints True
# d1 = {1:2, 3:4}
# d2 = {2:1, 4:3, 5:6}
# print(is_inverse(d1, d2))  # prints False
 
# d1 = {1:2, 3:4}
# d2 = {1:2, 2:1}
# print(is_inverse(d1, d2))  # prints False
def add_to_d(d, L):
    """ d is a dict
        L is a list of tuples
    Mutates d with new entries whose key is the first element of a 
    tuple in L and the associated value is the second element of a 
    tuple in L. If the key is already in d, do nothing to its value. 
    If the key cannot be added, raise a ValueError. Returns None. """
    pass
    
# d = {}
# L = [(1,2), (3,4)]
# add_to_d(d, L)
# print(d)   # d is mutated to be {1: 2, 3: 4}
# d = {1:1}
# L = [(1,2), (3,4)]
# add_to_d(d, L)
# print(d)   # d is mutated to be {1: 1, 3: 4}
# d = {1:1}
# L = [(3,4), ([1,2,3], 5)]
# add_to_d(d, L)   
# # raises a ValueError because its trying to add a list (mutable obj) as key
