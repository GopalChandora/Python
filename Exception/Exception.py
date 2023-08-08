a = 10
b = 5
print(a/b)
print('hello')

'''
a = 10
b = 0
print(a/b)
print('hello')

if we run the code it will give ZeroDivisionError for the line 10'''


'''
a = 10
b = 0
try :
	print(a/b)
except Exception:
	print('This is exception block')

print('hello')

To avoid the Error that we get it in 2nd code we used the try and except
 '''
 
'''
a = 10
b = 0
try :
	print('before operation')
	print(a/b)
	print('after operation')
except Exception as e:
	print('This is exception block',e)

This code will give two statements ouput as the line 35 will get neglect because the error has occured at line 34 and the try block will directly jump to except block skip the line 35
'''

'''
a = 10
b = 5
try :
	print('before operation')
	print(a/b)
	print('after operation')
except Exception as e:
	print('This is exception block',e)

This code will give three line output
'''
'''
a = 10
b = 0
try:
	print(a/b)
except ZeroDivisionError as e:
	print('Error is : ',e)
finally:
	print('Finally block')
'''
'''
x = 4
y = 20
try:
	print(y/x)
	n = int(input('Enter a number : '))
	print(n)# for value error
except Exception as e:
	print(' Error is : ',e)
finally:
	print('Finally block')
'''


'''
raise/throw a exception

num = input("Enter a number")

if num.isalpha():
    raise Exception("Enter integer number")

print("Hello")
'''