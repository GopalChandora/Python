from array import *

a = []
n = int(input('Enter size of array:\t'))

for i in range(n):
	print('Insert Element at:',i,end=' ')
	a.append(int(input()))

print('a before = ',a)

a1 = a.copy()
print('\n a1 before', a1)
a1.sort()
print('\n a1 after sort',a1)

for k in range(len(a)):
	for x in range(len(a1)):
		if a[k]==a1[x]:
			a[k]=x+1;
			break;
			
print('\n a after = ',a)
print('\n a1 after = ',a1)