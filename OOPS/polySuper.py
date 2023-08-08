class A:
    var1 = "class A variable"
    def __init__(self):
        self.var1 = "Class A Variable inside constructor"
        self.xyz = "hello A"


class B(A):
    var1 = "class B variable"
    def __init__(self):
        self.var1 = "Class B Variable inside constructor"
        super().__init__()

a = A()
b = B()
print(b.var1)
print(b.xyz)

'''
class grandfather:
    
    def home(self):
        print("I live in kharghar")

    def age(self):
        print("I am 50 yrs old")

class father(grandfather):
    
    def age(self):
        print("I am 30 yr old")
        
class son(father):
    def age(self):
        print("I am 20 yrs old")
        
s = son()
f = father()
s.home()
s.age()
f.age()
'''