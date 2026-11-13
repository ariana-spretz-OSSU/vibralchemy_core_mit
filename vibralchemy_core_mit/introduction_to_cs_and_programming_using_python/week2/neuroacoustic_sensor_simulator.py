"""
Design a simulator for Vibralchemy neuro-acoustic sensor. 
The program requests a frequency input via the console: 
if it is less than 4Hz, it prints "Delta Waves"; 
if it is between 4 and 7Hz, it prints "Theta Waves"; 
and if it is higher, it prints "Active State", 
applying clean code naming conventions.
"""
# Neuroacoustic Sensor Simulator

# Setting input variables
frequency = float(input("Enter a frequency number: "))

# Determine wave type based on frequency
if frequency < 4.0:
    print(f"{frequency} Hz: Delta Waves")
elif frequency >= 4.0 and frequency <= 7.0:
    print(f"{frequency} Hz: Theta Waves") 
elif frequency > 7.0:
    print(f"{frequency} Hz:Active State")

"""
Output example:
Enter a frequency number: 5
5.0 Hz: Theta Waves
"""


