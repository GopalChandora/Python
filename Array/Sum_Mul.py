from array import *

def add(arr):
    sum = 0
    mul = 1
    for k in arr:
        sum = sum + k
        mul = mul * k
    print("sun = ",sum)
    print("multiplication = ",mul)

a = array('i',[])
n = int(input("Enter Size of array : \t"))
for i in range(n):
    a.append(int(input("Enter Element = ")))

print("Elements are :")
for j in a:
    print(j)

add(a)

# sum = 0
# for k in a:
#     sum = sum + k
# print(sum)
