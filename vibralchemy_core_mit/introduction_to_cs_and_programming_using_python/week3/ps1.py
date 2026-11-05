import math

yearly_salary = float(input("Enter your yarly salary:"))
portion_saved = float(input("Enter the portion to be saved:"))
cost_of_dream_home = float(input("Enter the cost of your dream home:"))
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
numerator = math.log(cost_of_dream_home / amount_saved)
denominator = 12 * math.log(1 + r / 12)
months = numerator / denominator 
print(months)
