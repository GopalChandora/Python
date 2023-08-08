#Arguments: Information to be passed to a function

# Types of arguments:
    
# 1. Required Arguments
'''Required arguments are to be passed at the time of function call with the exact match of their positions in the function call and function definition
:
If either of the arguments is not provided in the function call, or the position of the arguments is changed, the Python interpreter will show the error.  '''

def add(c,d):
    return c+d
a = int(input("Enter value of a"))
b = int(input("Enter value of b"))

print("Addition is", add(a,b))

'''Output:
    Enter value of a 20
    Enter value of b 30
    Addition is 50    '''

# Case 1:

def add(c,d):
    return c+d

a = int(input("Enter value of a"))
b = int(input("Enter value of b"))

sum1 = add(a)
print("Addition is", sum1)

'''Output: 

    TypeError: add() missing 1 required positional argument: 'd'   ''' 

# Case 2:
def add(c,d):
    return c+d

a = int(input("Enter value of a"))
b = int(input("Enter value of b"))

sum1 = add(a,b)
print("Addition is", sum1)



# 2. Default Arguments
''' If the value of any of the arguments is not provided at the time of function call
then that argument can be initialized with the value given in the definition  '''
#case 1
def add(a,b = 20):
    return a+b

a = int(input("Enter value of a"))
print("Addition is", add(a))

#case 2
def add(a=1,b=2,c=3):
    return (a+b+c)
    
print(add(3))
print(add(3,4))
print(add(2,3,4))

'''Output:
Enter value of a 40
Addition is 60    '''

# 3. Keyword arguments

'''The name of the arguments is treated as the keywords and matched in the function calling and definition
If the same match is found, the values of the arguments are copied in the function definition
It allows us to pass arguments in random order and values given in function call cannot be changed '''


def string(name = "Pratik" , rollno = 20):
    print("My name is ", name, " and rollno is ", rollno)


string(name = "Saylee", rollno = 30)

'''Output:
My name is  Saylee  and rollno is  30  '''




# 4. Variable Length Arguments (*args)   (*Variable_name)

''' In the function call any number of values can be passed which are treated as tuple
In function definition, variable length argument is defined as *<Variable_Name>'''


def fun(*n):
    print("type of passed argument", type(n))
    print("printing the passed argumnets")
    print(n)
    for i in n:
        print(i)

fun("Mayuri", "Amitabh", "Hina")


'''Output:

type of passed argument <class 'tuple'>
printing the passed argumnets
Mayuri
Amitabh
Hina   '''
    


