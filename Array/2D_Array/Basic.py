from array import *

'''
# CASE 1
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr, "before")
 
arr[0][0] = 1 # update only one element
print(arr, "after")
'''

'''
# CASE 2 : Naive Method
r,c = (2,2)
a = [[1]*c]*r
print(a)
for r in a:
    for c in r:
        print(c,end=' ')
    print()
'''

'''
# CASE 3 : Using List Comprehension
r,c = (2,2)
a = [[1 for i in range(c)] for j in range(r)]
print(a)
'''

'''
# CASE 4
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for r in T:
   for c in r:
      print(c,end = " ")
   print()
'''


a = []
r = int(input("Enter Row Size : \t"))
c = int(input('Enter Column Size : \t'))
for i in range(r):
    col = []
    for j in range(c):
        print("Enter Element at ",i,j,": ",end=' ')
        col.append(int(input()))
    a.append(col)

for i in range(r): # i = 0 and i = 1
    for j in range(c): # j = 0,1 and j = 0,1 
        print(a[i][j],end= ' ') # m1 = [0,0] / [0,1] and m1 = [1,0] / [1,1]
    print()

#  Insertion 
con = int(input("Enter count of insertion : "))
for i in range(con):
    ind_value = int(input("Enter Index Value : "))
    data_value = list(input("Enter Elemnet : ").split())
    a.insert(ind_value,data_value)    

# for r in a: # r1 = [1,2] and [3,4]
#     for c in r: #1,2 and 3,4
#         print(c,end=' ') #1 2   3 4
#     print()

for i in range(r): # i = 0 and i = 1
    for j in range(c): # j = 0,1 and j = 0,1 
        print(a[i][j],end= ' ') # m1 = [0,0] / [0,1] and m1 = [1,0] / [1,1]
    print()