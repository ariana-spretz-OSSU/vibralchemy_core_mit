################ YOU TRY IT ################
# Write code that loops a for loop over some range 
# and prints how many even numbers are in that range. Try it with:
# range(5)
# range(10)
# range(2,9,3)
# range(-4,6,2)
# range(5,6)
#for i in range(5):
# your code here
count_even = 0
for i in range(5):
    if i % 2 == 0:
        count_even += 1
print(count_even)

# output: 3

count_even = 0
for i in range(10):
    if i % 2 == 0:
        count_even += 1
print(count_even)

# output: 5

count_even = 0
for i in range(2, 9, 3):
    if i % 2 == 0:
        count_even += 1
print(count_even)

# output: 2

count_even = 0
for i in range(-4, 6, 2):
    if i % 2 == 0:
        count_even += 1
print(count_even)

# output: 5

count_even = 0
for i in range(5, 6):
    if i % 2 == 0:
        count_even += 1
print(count_even)

# output: 0

#############################################

############### YOU TRY IT ####################
# Assume you are given a string of lowercase letters in variable s. 
# Count how many unique letters there are in s. For example, if 
# s = "abca" Then your code prints 3. 
# your code here
s = "the sun shines brightly over the blue sea today."
seen = ""
for char in s:
	if char not in seen:
	    seen += char
	        
print(len(seen))	

# Output: 18


##############################################

################ YOU TRY IT ##################
# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, it doesn't print anything. 
# your code here

secret_number = 4
if secret_number >= 1 and secret_number <= 10:
    print(secret_number)
elif secret_number == secret_number:
    print(secret_number)
else:
    print('')

################################################
#################### YOU TRY IT ###################
# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, prints that it didn't find it. 
# your code here   
secret_number = 4 
for num in range(11):
    if num == secret_number:
        print(secret_number)
    else:
        print('Secret number not found.')

####################################################

####################################################
##################### AT HOME ######################
######################################################
# Write code that counts how many unique common characters there are between 
# two strings. For example below, the common characters count is 8: 
# text1 = "may the fourth be with you"
# text2 = "revenge of the sixth"
# Hint, start to write your code with a smaller example, then test it on the above text.
# text1 = "abc"
# text2 = "cde"
# your code here

text1 = "The sun shines."
text2 = "Sun is shining."
seen_both = ""
for char in text1:
	for char in text2:
	    if char not in seen_both:
	        seen_both += char
print(len(seen_both))

# Output: 9

####################################################
##################### END AT HOME ######################
######################################################
