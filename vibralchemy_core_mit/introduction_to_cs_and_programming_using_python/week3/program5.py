"""
Program that automates a mathematical volume ladder for audio mixes

Exercise: Write a while loop that starts at a volume of 100 and decrements by 5 at each step, stopping strictly when it reaches zero.
"""
volume = 100
print("The starting volume is:", volume)

while volume and volume > 0:
    volume -= 5
    print("Volume now is:", volume)

"""
Output example:
The starting volume is: 100
Volume now is: 95
Volume now is: 90
Volume now is: 85
Volume now is: 80
Volume now is: 75
Volume now is: 70
Volume now is: 65
Volume now is: 60
Volume now is: 55
Volume now is: 50
Volume now is: 45
Volume now is: 40
Volume now is: 35
Volume now is: 30
Volume now is: 25
Volume now is: 20
Volume now is: 15
Volume now is: 10
Volume now is: 5
Volume now is: 0
"""