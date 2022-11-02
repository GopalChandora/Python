'''Syntax for (for loop)
for iterative_variable in sequence:
	statement'''
	
#code 1
L1=[10,20,30,40,50]
for i in L1:
	print(i)

# code 2
'''n = int(input('Enter a number :'))
for i in range(1,11):
	print(n,'*',i,'=',n*i)'''

#code 3
'''str='Gopal'
for i in range(len(str)):
  print(str[i])'''
  
#code 4
'''name='GopalChandora'
for i in range(5,13):
	print(name[i])'''
	
#code 5
'''for i in range(1,16):
if i%3==0:
	print(i,': is divisible by 3')
else:
	print(i,':is Not divisible by 3')'''

#code 6 break statement
'''for i in range(1,16):
	if i == 6:
		break
		print(i)
	else:
		print(i)'''
		
#code 7 continue statement 
'''for i in range(1,5):
	if i == 3:
		continue
		print(i)
	else:
		print(i)'''
