# Recursive Function:
# Program to calculate factorial of a number

def recur_factorial(n):  # n = 1
   if n == 1:
      return n  
   else:  
      return n*recur_factorial(n-1)  
  
num = int(input("Enter a number: "))   
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))

# Program to display Fibonacci series

def fibo(n):
   if n <= 1:
      return n
   else:
      return(fibo(n-1) + fibo (n-2))   # return(fibo(2) + fibo(1))  # return(1 + 1) 

no_of_terms  = int(input("Enter no of terms you want to display:"))
if no_of_terms <= 0:
   print("Enter positive term")
else:
   print("Fibonacci Series: with ", no_of_terms, "Terms")
   for i in range(no_of_terms):
      print(fibo(i))    # fibo(3)

'''      
i = 0  to 14
i = 0
fibo(0)   =   0
i = 1
fibo(1)   =   1
i = 2
fibo(2)   =   1
i = 3
fibo(3)    =   2
'''
                 


# Lambda Function:

''' It is an anonymous function defined without a name
lambda keyword is used to declare this function  '''

# Syntax:
'''
lambda arguments: expression
''' 
x = lambda a:a+10    # a = 20
# printing the function object  
print(x)  
print("sum = ",x(20))

# Using filter() function:
''' It accepts a function and a list as an argument
Used to filter out all elements of the sequence returning the new sequence '''

list1 = (10,22,37,41,100,123,29)
evenlist = tuple(filter(lambda x:(x%2 == 0),list1)) 
print(evenlist)

# using map() function:
''' It accepts a function and a list as an argument ''' 
t1 = (10,20,30,40,50,60)  
square = list(map(lambda x:x**2,t1))   
print(square)  
