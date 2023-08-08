class car:
#   name = "BMW"
#   price = "1cr"
  def __init__(self,name,price):
    self.name = name
    self.price = price

  def cardetails(self):
    return f" name is {self.name} and price is {self.price}" # f string 

cr = car(1,2)
# cr.name = "BMW"
# cr.price = "2cr"
# print(cr.name)
# print(cr.price)
#print(cr.__dict__) #return a dictionary 
print(cr.cardetails())