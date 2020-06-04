# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
month = 0

while principal > 0:
	#adds month
    month+=1 #month = 2
    #checks condition for extra payment
    #for month 1 - extra_payment_start_month c_payment = 2684.11
    #for month extra_payment_start_month - extra_payment_end_month c_payment = 3684.11
    if month>=extra_payment_start_month and month <= extra_payment_end_month:
        c_payment = payment + extra_payment 
    else:
        c_payment = payment
    #checks for negative principal
    if c_payment >= principal*(1+rate/12):
    	c_payment = principal*(1+rate/12)
    	principal = principal*(1+rate/12) - c_payment 
    	total_paid += c_payment
    	print(f'month: {month} total paid:{total_paid:0.2f} principal:{principal:0.2f}')
    else:
    	principal = principal * (1+rate/12) - c_payment
    	total_paid = total_paid + c_payment
    	print(f'month: {month} total paid:{total_paid:0.2f} principal:{principal:0.2f}')