''' Syntax to create class 
class class_name:
	statement 1
	....
	statement n
**classes are like as blueprint or temolate for object

Syntax to create object 
Object_name = class_name()

Object are also called as instance of class

Non Parameterized Constructor
class class_name:
	def __init__():
	def.function_name(parameter):

obj_name  = class_name()
obj.function_name(parameter)

Parameterized Constructor
class class_name:
	def __init__(parameter):
	def.function_name():

obj_name  = class_name(parameter)
obj.function_name()
'''


# code  1
class student:
	def __init__(self,name,rollno,age):
			self.name= name
			self.rollno = rollno
			self.age= age
	def display(self):
		print('\nName =',self.name)
		print('\nRollno =',self.rollno)
		print('\nAge=',self.age)
		
st1 = student('gopal',1,20)
st2 = student('Arvind',2,21)

@classmethod
def yash_str(cls,string):
	list1 = string.split(",")
	print(list1)
	return cls(list1[0],list1[1],list1[2])
	

st1.display()
st2.display()
yash = student.yash_str("Yash,3,23")
# we can give any name at self.name

# code 2
# count no of object 
class student:
	count=0
	def __init__(self):
		student.count = student.count+1
		
st = student()
st = student()
print(student.count)

#code 3
# Non - Parameterized Constructor
class student :
	def __init__(self):
#	def __init__(self,name,rollno):
#		self.name = name
#		self.rollno = rollno
		print('In Non - Parameterized Constructor')
#		print('name',name)
#		print('rollno',rollno)
	
	def display(self,rollno,name):
		print('Name : ',name,'Rollno :',rollno)
	
#st = student('arvind',1)
st = student()
st.display(10,'gopal')
''' Here we have to give parameter to display and given the agruments at st.display()
'''
#code 4:
#Parameterized Constructor
class student:
	def __init__(self,name,rollno):
		self.name = name
		self.rollno = rollno
		print('In Parameterized Constructor')
	def display(self1):
		print('name :',self1.name)
		print('Roll no:',self1.rollno)
		
st = student('gopal',31)
st.display()

''' If we use parameter in constructor then we have to give arguments in object creation and at printing we have to use self1.name '''