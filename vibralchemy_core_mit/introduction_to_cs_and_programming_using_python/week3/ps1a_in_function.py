def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0
	r = 0.05
	target_savings = cost_of_dream_home * portion_down_payment
	amount_to_be_saved = (yearly_salary / 12) * portion_saved
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while amount_saved < target_savings:
	    monthly_return = amount_saved * (r/12)
	    amount_saved += monthly_return + amount_to_be_saved
	    months += 1
	
	print("Number of months:", months)
	
	return months