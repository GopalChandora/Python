'''
 * * * * *
  * * * *
   * * *
    * *
     *
'''

for i in range(5,0,-1):
    for k in range(0,5-i):
        print(end = " ")
    for j in range(0,i):
        print("*",end = " ")
    print()
'''
num = int(input("Enter number of row"))
for i in range(num,0,-1):
    for k in range(0,num-i):
        print(end = " ")
    for j in range(0,i):
        print("*",end = " ")
    print()
'''
