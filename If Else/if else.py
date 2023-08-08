''' Syntax of if else 
if expression:
	statement
else :
	statement '''
	
age = int(input('Enter your age :'))
if age >=18:
	print('Eligible for vote because age is:',age)
else :
	print('You are not eligible because your age is :',age)