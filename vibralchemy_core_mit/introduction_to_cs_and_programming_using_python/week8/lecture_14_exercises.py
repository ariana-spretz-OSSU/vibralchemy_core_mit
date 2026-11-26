################## YOU TRY IT #########################
def find_grades(grades, students):
    """ grades is a dict mapping student names (str) to grades (str)
        students is a list of student names 
    Returns a list containing the grades for students (in the same order) """
    # your code here
    student_list = []
    for student in students:
        student_list += grades[student]
    return student_list
d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # Output: ['C', 'A']

########################################################
################## YOU TRY IT #########################
def find_in_L(Ld, k):
    """ L is a list of dicts
        k is an int
    Returns True if k is a key in any dicts of L and False otherwise """
    # your code here
    for i in Ld:
        if k in i:
            return True
    return False
d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
print(find_in_L([d1, d2, d3], 2))  # Output: True
print(find_in_L([d1, d2, d3], 25))  # Output: False
########################################################
########################### YOU TRY IT ######################
def count_matches(d):
    """ d is a dict
    Returns how many entries in d have the key equal to its value """
    count = 0
    for k, v in d.items():
        if k == v:
            count += 1
    return count
        
d = {1:2, 3:4, 5:6}
print(count_matches(d))   # Output: 0
d = {1:2, 'a':'a', 5:5}
print(count_matches(d))   # Output: 2
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
        all_data = all_data + data[stud][what]
        # B) all_data.append(data[stud][what]) 
        # C) all_data = all_data + data[stud[what]]
        # D) all_data.append(data[stud[what]]) 
    return sum(all_data)/len(all_data)
print(get_average(my_d, 'mq') )   # Output: 7.0
###########################################################

######################################################
############## AT HOME ###################
######################################################
def is_inverse(d1, d2):
    """ d1 and d2 are dicts 
    Assume values of d1 and d2 are unique and immutable
    Returns True if d1's keys are values in d2 and d1's 
    values are keys in d2 """
    if len(d1) != len(d2):
        return False
    
    for k, v in d1.items():
        if v not in d2 or d2[v] != k:
            return False
    return True

d1 = {1:2, 3:4}
d2 = {2:1, 4:3}
print(is_inverse(d1, d2))  # Output: True
d1 = {1:2, 3:4}
d2 = {2:1, 4:3, 5:6}
print(is_inverse(d1, d2))  # Output: False
 
d1 = {1:2, 3:4}
d2 = {1:2, 2:1}
print(is_inverse(d1, d2))  # Output: False

def add_to_d(d, L):
    """ d is a dict
        L is a list of tuples
    Mutates d with new entries whose key is the first element of a 
    tuple in L and the associated value is the second element of a 
    tuple in L. If the key is already in d, do nothing to its value. 
    If the key cannot be added, raise a ValueError. Returns None. """
    for k, v in L:
        try:
            if k not in d:
                d[k] = v
        except TypeError:
            raise ValueError

d = {}
L = [(1,2), (3,4)]
add_to_d(d, L)
print(d)   # Output: {1: 2, 3: 4}

d = {1:1}
L = [(1,2), (3,4)]
add_to_d(d, L)
print(d)   # Output: {1: 1, 3: 4}

d = {1:1}
L = [(3,4), ([1,2,3], 5)]
add_to_d(d, L)   
# Output: raises a ValueError because its trying to add a list (mutable obj) as key