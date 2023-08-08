class college:
    def __init__(self,name,cname,caddres):
        self.name = name
        self.cname = cname
        self.caddres = caddres
    
class student(college):
    def stdbio(self):
    # def stdbio(self,name,addres):
    #     self.name = name
    #     self.addres = addres
        return f"{self.name} study in {self.cname} college {self.caddres}"

objg = student("Gopal","Terna","Nerul")
print(objg.stdbio())