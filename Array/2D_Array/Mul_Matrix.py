m1 = []

r1 = int(input("Enter Row Size : \t"))
c1 = int(input("Enter Column Size : \t"))

for i in range(r1):
    col1 = []
    for j in range(c1):
        print("Enter Element at ",i,j," : ",end = ' ')
        col1.append(int(input()))
    m1.append(col1)

print("Matrix is : ")
for i in range(r1):
    for j in range(c1):
        print(m1[i][j],end=' ')
    print()

print("Second Matrix Data.")
m2 = []
r2 = int(input("Enter Row Size : \t"))
c2 = int(input("Enter Column Size : \t"))

for i in range(r2):
    col2 = []
    for j in range(c2):
        print("Enter Elemnet at ",i,j," : ",end = ' ')
        col2.append(int(input()))
    m2.append(col2)

print("Matix is : ")
for i in range(r2):
    for j in range(c2):
        print(m2[i][j], end = ' ')
    print()

m3 = []
for i in range(r1):
    for j in range(c1):
        x = []
        for k in range(r2):
            x.append(m1[i][j]*m2[j][k])
        m3.append(x)

print(m3)
