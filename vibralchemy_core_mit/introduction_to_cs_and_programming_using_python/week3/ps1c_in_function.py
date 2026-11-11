def part_c(initial_deposit):
	#########################################################################
	cost_of_the_house = 800000
	down_payment = cost_of_the_house * 0.25
	target_savings = down_payment
	months = 36
	low = 0.0
	high = 1.0
	epsilon = 100
	r = (low + high) / 2
	amount_saved = 0
	steps = 0
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	if initial_deposit >= target_savings - 100:
	    r = 0.0
	    steps = 0
	else:  
	    while abs(amount_saved - target_savings) > epsilon and (high - low) > 0.0001:
	        amount_saved = initial_deposit * (1 + (r / 12))**months
	        if amount_saved < target_savings:
	            low = r
	        else:
	            high = r
	        r = (low + high) / 2
	        steps += 1   
	
	if amount_saved < target_savings - epsilon:
	    r = None
	
	if r == None:
	    print("The best savings rate: None")
	else:
	    print(f'The best savings rate: {r / 10000.0}')
	    
	print(f'Steps in bisection search: {steps}')
	return r, steps