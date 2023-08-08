# Function:
'''
Function is a block of code where instructions are written to perform a task assigned to a function
It is executed when it is called    '''

# Two Types of Functions:
'''
1. Built in function:  Predefined functions in python
2. User Defined Function: defined by user to perform a task '''

#syntax of function
'''
def function_name(parameters):     #function def
    statement1
    stetement2
    return expression

function_name(parameters)              #function call '''

def add(x,y):
	print('Addition of ',x,'+',y,'=',x+y)
	
num1=int(input('Enter first number : '))
num2=int(input('Enetr second number : '))
add(num1,num2)

#WITH RETURN 

'''def add(x,y):
	return x+y
num1=int(input('Enter first number : '))
num2=int(input('Enter second number : '))
result=add(num1,num2)
print('Addition of ',num1,'+',num2,'=',result)'''

'''def add(c,d):
   print("Value of c:", c)
   print("Value of d: ",d)
   return c+d

a = int(input("Enter value of a:"))
b = int(input("Enter Value of b:"))
print("Addition of a and b is : ", add(a,b))

Output:
Enter value of a: 50
Enter Value of b: 60
Value of c: 50
Value of d:  60
Addition of a and b is :  110'''
   

#  Call by value

'''def add(c,d):
    print("Value of c = ",c)
    print("Value of d = ", d)
    c = 100
    d = 200
    print("Value of c = ",c)
    print("Value of d = ", d) 
    return c+d


a = int(input("Enter value of a"))
b = int(input("Enter value of b"))

sum1 = add(a,b)
print("Addition is", sum1)'''


# Call by Reference
'''def modify(list2):
    list1.append(50)
    list1.append(60)
    print("Modified List1 = ", list2)

list1 = [10,20,30,40]

modify(list1)
print("List1 = ", list1)'''


'''def modify_str(str1):
   str1 = str1 + "Welcome to Python LEcture"
   print("Modified string is", str1)

str1 = "Leena"
modify_str(str1)
print("string is :", str1)'''

# upper and lower case count
'''def count_upper_lower(str):
	dic = { 'upper_case':0,'lower_case':0}
	for i in str:
		if i.isupper():
			dic['upper_case']+=1
		else:
			dic['lower_case']+=1
			
	print(dic)

str  = input('Enter a string : ')
print('Entered string is : ',str)
count_upper_lower(str)
'''

