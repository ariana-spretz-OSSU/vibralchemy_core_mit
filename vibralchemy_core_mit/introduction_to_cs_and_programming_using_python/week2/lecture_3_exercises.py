################ YOU TRY IT ###################
## EXAMPLE: infinite loop, be careful!
# To stop it, click the shell and hit CTRL+c or 
# the red square at the top of the shell
##############################################
# while True:
#     print("noooooooo")
############### YOU TRY IT ###################
# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
##############################################
# where = input("Go left or right? ")
# while where == "right":
#     where = input("Go left or right? ")
# print("You got out!")

where = input("Go left or right? ")
count = 0
while where == "right":
    count += 1 
    where = input("Go left or right? ")
    if count >= 2:
        print(":C")
print("You got out!")

"""
Output:
Go left or right? right
Go left or right? right
Go left or right? right
:C
Go left or right? left
:C
You got out!
"""
##############################################

################ YOU TRY IT ################
# for i in range(1,4,1):
#     print(i)
# for j in range(1,4,2):
#     print(j*2)
# for me in range(4,0,-1):
#     print("$"*me)

"""
Output:
1
2
3
2
6
$$$$
$$$
$$
$
"""
############################################

################ YOU TRY IT ################
# Fix this code to use variables start and end in the 
# range, to get the total sum between and including those values. 
# mysum = 0
# start = 3
# end = 5
# for i in range(start, end):
#     mysum += i
# print(mysum)

mysum = 0
start = 3
end = 5
for i in range(start, end + 1):
    mysum += i
print(mysum)

"""
Output:
12
"""
###########################################
#########################################################
##################### AT HOME ###########################
#########################################################
# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. 
# For ex. if x = 14, it prints 5 and 10.
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. 
# For ex. if x = 14, it prints 5 and 10.

x = int(input("Enter a positive number: "))
print(x)    
while x >= 1 and x % 5 == 0:
    x -= 5
    if x == 0:
        break
    print(x)

"""
Output:
Enter a positive number: 55
55
50
45
40
35
30
25
20
15
10
5
"""

# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits 
# in n. Hint: you can get a digit at a time looking at the remainder 
# when you divide n by 10.
# For ex. If x = 1234, print 1

n = input("Enter an integer number: ")
sum = 0
for i in range(len(n)):
    num = n[: 1]
    digit = int(num)
    sum += digit
    rest_num = n[1:]
    n = rest_num
    if n == 0:
        break
print(sum)

"""
Output:
Enter an integer number: 1989
27
"""
#########################################################
##################### END AT HOME ###########################
#########################################################