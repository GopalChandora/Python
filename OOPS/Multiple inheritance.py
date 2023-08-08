class Sum :
	def sum1(self,x,y):
		return x+y
class Mul:
	def mul1(self,x,y):
		return x*y
class Sub:
	def sub1(self,x,y):
		return x-y
class result(Sum,Mul,Sub):
	def res1(self):
		return 0
		
r = result()
print(r.sub1(15,10))
print(r.sum1(15,10))
print(r.mul1(15,10))
