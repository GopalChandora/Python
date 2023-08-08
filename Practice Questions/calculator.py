def Add(x,y):
	print('Addition of ',x,'+',y,'=',x+y)
def Sub(x,y):
	print('Subtraction of ',x,'-',y,'=',x-y)
def Mul(x,y):
	print('Multiplication of ',x,'*',y,'=',x*y)
def Div(x,y):
	print('Division of ',x,'/',y,'=',x/y)
	
	
a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
ch= int(input('Press \n1 Add \n2 Sub \n3 Mul \n4 Div'))

while True  :
	if (ch == 1):
	   Add(a,b)
	elif (ch == 2):
		Sub(a,b)
	elif (ch == 3):
		Mul(a,b)
	elif (ch == 4):
		Div(a,b)
	else :
		print('EXITED...')

	
'''
Python Program to Convert Decimal to Binary, Octal and Hexadecimal using functions
'''