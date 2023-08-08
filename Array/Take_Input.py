from array import *

a = array('i',[])

n = int(input("Enter size of array : \t"))

for i in range(n):
    x = int(input("Enter Value : \t"))
    a.append(x)
    
print(a)