class A:
    def met(self):
        print("I am in class A")

class B(A):
    def met(self):
        print("I am in class B")
        
class C(A):
    def met(self):
        print("I am in class C")

class D(B,C):
    def met(self):
        print("I am in class D")
       
a = A()
b = B()
c = C()
d = D()
d.met()

'''
Dunder method started with ( __ )
example - __init__() or __truediv__() or __add__() etc

class A:
    def __init__(self,age):
        self.age = age
    def __add__(self,other):
        return self.age + other.age

class B:
    def __init__(self,age):
        self.age = age
    
    
a = A(50)
b = B(40)
print(a+b)
'''

'''
extra dunder method
class A:
    def __init__(self,age):
        self.age = age
    
    def __add__(self,other):
        return self.age + other.age
    
    def __repr__(self):
        return f"Age = ({self.age})"

    def __str__(self):
        return f"Age = {self.age}"
    
a = A(50)
b = A(40)
print(repr(a))
'''