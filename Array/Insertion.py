from array import *

a = array('i',[])
# a = []
n = int(input("Enter Size of array : \t"))
for i in range(n):
    a.append(int(input("Enter Element = ")))

# Insertion of Element in Array from user's (index,value)
a1 = array(a.typecode,[])
print("Insert Elemnet :")
for i in range(len(a)):
    ind_value = int(input('Enter index value : '))
    data_value = int(input('Enter Value to insert: '))
    a.insert(ind_value,data_value)
    # print("Inserted : ",a[ind_value])
    a1.append(a[ind_value])

print("Inserted Element : ", end = ' ')
for i in a1:
    print(i,end=' ')

print("\nArray A = ", end =' ')
for j in a:
    print(j, end = ' ')

'''
#  Insertion in array
key = array(a.typecode,[10,20,30])
print("Inserted Elemnet = ", end= ' ')
for i in range(len(a)):
    a.insert(i,key[i])
    print(a[i],end=' ')

print("\nArray A = ", end =' ')
for j in a:
    print(j, end = ' ')
'''
