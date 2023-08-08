from array import *

def rev(n):
	start = 0
	end = n-1
	for k in range(len(a)):
		a[start],a[end] = a[end],a[start]
		start+1
		end-1
	
a = array('i',[])
n = int(input('Enter Size of array:\t'))

for i in range(n):
	print('Insert element at:',i,'\t',end=' ')
	a.append(int(input()))

for j in range(len(a)):
	print(a[j])

x = rev(n)
print(a)

#print(a[::-1]) #Reverse by slicing