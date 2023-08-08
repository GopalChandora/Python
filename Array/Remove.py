from array import *

a = array('i',[])
# a = []
n = int(input("Enter Size of array : \t"))
for i in range(n):
    a.append(int(input("Enter Element = ")))

# Insertion of Element in Array from user's (index,value)
a1 = array(a.typecode,[])
print("Remove Elemnet :")
Remonum = int(input("Enter no of Element to be removed : ")) 
for i in range(Remonum):
    data_value = int(input('Enter Value to remove: '))
    a.remove(data_value)
    a1.append(data_value)

print("Removed Element : ", end = ' ')
for i in a1:
    print(i,end=' ')

print("\nArray A = ", end =' ')
for j in a:
    print(j, end = ' ')
