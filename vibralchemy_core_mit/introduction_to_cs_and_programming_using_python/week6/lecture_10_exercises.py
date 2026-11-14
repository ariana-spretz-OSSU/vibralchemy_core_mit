############# YOU TRY IT #####################
# What is the value of L1, L2, L3, and L after these commands?
# L1 = ['re']
# L2 = ['mi']
# L3 = ['do']
# L4 = L1 + L2
# L3.append(L4)
# L = L2.append(L3)
#################################################
############### YOU TRY IT #######################
# Write a function that meets the specification:
def make_ordered_list(n):
 """ n is a positive int
 Returns a list containing all ints in order
 from 0 to n (inclusive)
 """
 # your code here

#print(make_ordered_list(6)) # prints [0, 1, 2, 3, 4, 5, 6]
#####################################################
############ YOU TRY IT ###############
def remove_elem(L, e):
 """
 L is a list
 Returns a new list with elements in the same order as L
 but without any elements equal to e.
 """
 # your code here

# L = [1,2,2,2]
# print(remove_elem(L, 2)) # prints [1]
# L = [1,2,2,2]
# print(remove_elem(L, 1)) # prints [2,2,2]
# L = [1,2,2,2]
# print(remove_elem(L, 0)) # prints [1,2,2,2]

####### YOU TRY IT ###################
# Write a function that meets this specification
def count_words(sen):
 """ sen is a string representing a sentence
 Returns how many words are in sen (i.e. a word is a
 a sequence of characters between spaces. """
 # your code here
# s = "Hello it's me"
# print(count_words(s)) # prints 3
# s = "I just took a DNA test turns out I'm 100% splitting strings"
# print(count_words(s)) # prints 12
###########################################

############## YOU TRY IT #################
# Write a function that meets this specification
def sort_words(sen):
 """ sen is a string representing a sentence
 Returns a list containing all the words in sen but
 sorted in alphabetical order. """
 # your code here
# s = "look at this photograph"
# print(sort_words(s)) # prints ['at', 'look', 'photograph', 'this']
# s = "now this is a story all about how my life got flipped turned upside down"
# print(sort_words(s))
##########################################

#######################################
############ AT HOME ###############
#######################################
## Question 1
# L1 = ['re']
# L2 = ['mi']
# L3 = ['do']
# L4 = L1 + L2
# L3.extend(L4)
# L3.sort()
# del(L3[0])
# L3.append(['fa', 'la'])
# What's the value of L3 here?
## Question 2
# L1 = ['bacon', 'eggs']
# L2 = ['toast', 'jam']
# brunch = L1
# L1.append('juice')
# brunch.extend(L2)
# What's the value of brunch here?
## Question 3.
def apply_to_each(L, f):
 """ L is a list of numbers
 f is a list that takes in a number and returns a number
 Mutate L such that you apply function f to every element in L """
 # your code here
# test = [1,-2,3]
# apply_to_each(test, lambda x: x**2)
# print(test) # prints [1,4,9]
# test = [-7, 8, 5, -8, -3]
# apply_to_each(test, abs)
# print(test) # prints [7, 8, 5, 8, 3]

