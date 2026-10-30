"""Write a script that processes YouTube SEO title strings. 
The program iterates through the string to clean up unnecessary spaces, 
manually counts characters, and uses simple guessing logic 
to validate whether it contains keywords."""
SEO_titles = "solfeggio frequencies, meditation music, binaural beats, healing sounds, relaxation, stress relief, sleep aid, chakra balancing, mindfulness, spiritual awakening"
titles = input("Enter a YouTube SEO title: ")

sentence = "The sun  shines."
new_sentence = sentence.split()
print(new_sentence)

join_sentence = ""
for word in new_sentence:
    join_sentence += word + " "
    whole_sentence = join_sentence[:-1]
print(whole_sentence)

lengh_sentence = len(whole_sentence)
print(lengh_sentence)

if titles in SEO_titles:
    print("SEO is correct")
else:
    print("SEO is incomplete")



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