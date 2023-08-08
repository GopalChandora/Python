'''
     *
    * *
   * * *
  * * * * 
 * * * * *
  * * * *
   * * *
    * *
     *
'''
k = 1
y = 2
for i in range(5):
    for x in range(5-i):
        print(end = " ")
    for j in range(k):
        print("*",end = " ")
    k = k+1
    print()
for l in range(4,0,-1):
    for m in range(4-y):
        print(end = " ")
    for n in range(0,l):
        print("*",end = " ")
    y = y-1
    print()
