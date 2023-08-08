import numpy as n 

'''syntax of array :- 
var_name = n.array( [ data ] )'''

# code 1
b = n.array([1,2,3,4,5,6]) #inisilaization
print(b) #printing 
print(type(b))# print the type
print(b[0]) 


# code 2
import numpy

print('\n 1D array')
a = numpy.array([1,2,3,4,5,6])
print(a)
print(type(a)) # check type
print(a[1]+a[4])# addition of number at specified index

# code 3
print('\n 2D Array')
c = n.array([[1,2,3],[4,5,6]]) 
print(c)
print(c.ndim) # check dimension


# code 3
print('\n 3D Array')
d = n.array([ [[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]] ]) 
print(d)
print(c.ndim) # check dimension

'''
import numpy as np

a = np.array([1,2,3,4,5]) 
b = np.array([[1,2,3,4],[4,5,6,7]])
print(a)
print(a.ndim)
print(a[0]) # index value
print(b[1,2]) # first index and then second index in 1st index
print(a[1:4]) # slicing
print(b[1,1:4])

x = a.copy() #changes made in copy not affect original array and changes made in original not affect copy
a[0] = 10
print(x)
print(a)

y = a.view() #changes made in view affect original array and changes made in original affect view
a[0] = 1
print(a)
print(y)

for i in a:
    print(i)
'''