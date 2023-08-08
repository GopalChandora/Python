from array import *

a = array('i',[])
n = int(input("Enter Size of array : \t"))
for i in range(n):
    a.append(int(input("Enter Element = ")))

print("Elements are :")
# for j in a:
#     print(j) # Print directly from a 

for j in range(len(a)):
    print(a[j]) # printing from index value

# Finding Index through Element
key = int(input("Enter Elemnet to find :"))
for k in range(len(a)):
    if a[k] == key:
        print(f"Value {key} is at {k}")

# # Finding Element through Index
# key = int(input("Enter index to find element : "))
# for k in range(len(a)):
#     if k == key:
#         print(f" Index {key} has value {a[k]}")


'''
# Using List
a = []
n = int(input("Enter Size of array : \t"))
for i in range(n):
    x = input("Enter Element = ")
    a.append(x)

key = input("Enter value :")

for k in range(len(a)):
    if key == a[k]:
        print(f" value {key} is at {k}")\

'''