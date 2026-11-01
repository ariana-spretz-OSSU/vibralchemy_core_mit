"""Write a script that processes YouTube SEO title strings. 
The program iterates through the string to clean up unnecessary spaces, 
manually counts characters, and uses simple guessing logic 
to validate whether it contains keywords."""

# Setting variables
SEO_titles = "solfeggio frequencies, meditation music, binaural beats, healing sounds, relaxation, stress relief, sleep, aid, chakra balancing, mindfulness, spiritual awakening"
title = input("Enter a YouTube SEO title: ")

# Cleaning user input
title_lowercase = title.lower()
title_strip_spaces = title_lowercase.strip()
# TODO/DEBUG: Print to verify result
# print(title_strip_spaces)

title_cleaned = title_strip_spaces.split()
# TODO/DEBUG: Print to verify result
# print(title_cleaned)

sentence = " ".join(title_cleaned)
# TODO/DEBUG: Print to verify result
# print(sentence)

lengh_title = len(sentence)
# TODO/DEBUG: Print to verify result
# print(lengh_title)

# Showing results to the user
if lengh_title >= 100:
    print("Alert! title lengh is too long.")
if lengh_title >= 60:
    print("The whole title is not seen on the screen.")
else:
    print("The whole title is seen on the screen.")

if sentence in SEO_titles:
    print("SEO is correct.")
else:
    print("SEO is not correct.")

"""
Output example:
Enter a YouTube SEO title:       mediTation   muSic  
meditation   music
['meditation', 'music']
meditation music
16
The whole title is seen on the screen.
SEO is correct.
"""


"""count_even = 0
for i in range(2, 9, 3):
    if i % 2 == 0:
        count_even += 1

count_even = 0
for i in range(-4, 6, 2):
    if i % 2 == 0:
        count_even += 1

s = "the sun shines brightly over the blue sea today."
seen = ""
for char in s:
	if char not in seen:
	    seen += char
	        
print(len(seen))	

# 18

text1 = "The sun shines."
text2 = "Sun is shining."
seen_both = ""
for char in text1:
	for char in text2:
	    if char not in seen_both:
	        seen_both += char
print(len(seen_both))

# 9

secret_number = 51
for num in range(11):
    if num == secret_number:
        print(secret_number)
    else:
        print('')	

"""



