class base:
	def __init__(self):
		self.a=5
class derived(base):
	def __init__(self):
		base.__init__(self)
		print("Derived Base class",self.a)
		self.a=3
		print("Derived class",self.a)

obj1 = base()
obj2 = derived()
print("base class P ",obj1.a)
print("derived class P ",obj2.a)