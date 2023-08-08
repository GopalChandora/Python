from array import *

def findMaxMin(arr):
    m = len(arr)
    if m == 0:
        print("Empty array")
    elif m == 1:
        print("max and min =", a[0])
    elif m > 2:
        maximum = a[0] 
        for i in range(n):
            if a[i] > maximum: 
                maximum = a[i] 
            else:
                minimum = a[i] 
        return (maximum,minimum)
        # print("max = ",maximum)
        # print("min = ",minimum)
    else:
        if arr[0] > arr[1]:
            maximum = a[0]
            minimum = a[1]
            return (maximum,minimum)
            # print("max = ",a[0])
            # print("min = ",a[1])
        else:
            maximum = a[1]
            minimum = a[0]
            return (maximum,minimum)
            # print("max = ",a[1])
            # print("min = ",a[0])
    #print("max = ", maximum)
    #print("min = ",minimum)

a = array('i',[])
n = int(input("Enter size of array: \t "))
for i in range(n):
    {
        print("Enter Element at :",i, end=" "),
        a.append(int(input()))
    }

for i in range(n):
    print(a[i], end=" ") # 0/1, 1/2, 2/3 (i/value)

mx,mn = findMaxMin(a)
print("Maximum number = ",mx)
print("Minimum number = ",mn)

# print(min(a)) # using built in min function
# print(max(a)) # using built in max function

# maximum = a[0] #1
# for i in range(n):
#         if a[i] > maximum: # 1<1, 2<1, 3<2
#             maximum = a[i] # 1/2, 2/3
#         else:
#              minimum = a[i] # 0/1
# print(maximum) 
# print(minimum)