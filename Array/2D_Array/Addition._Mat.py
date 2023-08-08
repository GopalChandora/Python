print(" For Matrix First : ")
m1 = []
r1 = int(input("Enter Size of row : \t"))
c1 = int(input("Enter size of column : \t"))

for i in range(r1):
    col1= []
    for j in range(c1):
        print("Enter Element at ",i,j,": ",end=' ')
        col1.append(int(input()))
    m1.append(col1)

# for r1 in m1: # r1 = [1,2] and [3,4]
#     for c1 in r1: #c1 = 1,2 and 3,4
#         print(c1,end = ' ') # 1 2   3 4
#     print()

print("First Matrix is : ")
for i in range(r1): # i = 0 and i = 1
    for j in range(c1): # j = 0,1 and j = 0,1 
        print(m1[i][j],end= ' ') # m1 = [0,0] / [0,1] and m1 = [1,0] / [1,1]
    print()


print("For Matrix Second : ")
m2 = []
r2 = int(input("enter row size : "))
c2 = int(input("Enter Column size : "))

for i in range(r2):
    col2 = []
    for j in range(c2):
        print("Enter Element at ",i,j,": ",end=' ')
        col2.append(int(input()))
    m2.append(col2)

print("Second Matrix is : ")
for i in range(r2):
    for j in range(c2): 
        print(m2[i][j],end= ' ')
    print()

m3 = []
if r1 == r2 and c1 == c2:  
    for i in range(r1):
        x = []
        for j in range(c1):
            x.append(m1[i][j]+m2[i][j])
        m3.append(x)

    print("Addition of matrices is : ")
    for i in range(r1):
        for j in range(c1):
            print(m3[i][j],end = ' ')
        print()

else:
    print("Matrix should be symmetrical ")