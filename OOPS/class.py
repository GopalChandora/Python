'''
# class operation:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def addition(self):
#         print(self.a+self.b)
    
#     def multiplication(self):
#         print(self.a*self.b)   

# class operation1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def substraction(self):
#         print(self.a-self.b)
    
# obj = operation(10,20)
# obj.addition()
# obj.multiplication()

# obj = operation1(50,100)
# obj.substraction()

# obj1 = operation(100,20)
# obj1.addition()
# obj1.multiplication()

# obj1 = operation1(10,20)
# obj1.substraction()
'''

'''
class vehical:
    def __init__(self,name,max_speed,mileage,no_pass):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.no_pass = no_pass 

    def fare(self):
        print("fare = ",self.no_pass*50)

obj=vehical("BMW",60,20,50)
obj.fare()
'''

class car:
#   name = "BMW"
#   price = "1cr"
  def __init__(self,name,price):
    self.name = name
    self.price = price

  def cardetails(self):
    return f" name is {self.name} and price is {self.price}" # f string 

cr = car("BMW","2Cr")
# cr.name = "BMW"
# cr.price = "2cr"
# print(cr.name)
# print(cr.price)
#print(cr.__dict__) #return a dictionary 
print(cr.cardetails())