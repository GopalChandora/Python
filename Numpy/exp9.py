import numpy as n

array = n.array( [ 1,2,3,4,5,6,7,8,9,10 ] )
array1 = n.array( [ [10,11,12],[13,14,15] ] )
array3 = n.array( [ 16,18,20,17,19 ] )
array4 = n.array( [ 20,21,22 ],dtype = complex)
array5 = n.array( n.mat('25,26;27,28'), subok = True)

print('Array =',array)

print('\nArray 1 = \n',array1)

print('\nArray Type :- ',type(array))

print('\nSize of Array :- ',array.ndim,' Dimensional')

print('\n Shape of array1 = ',array1.shape)

print('\nAddition of Array =',array[3]+array[5])

print('\nArray 3 = ',array3)

print('\nSorted Array 3 = ',n.sort(array3))

print('\n Size of array3 = ',array3.size)

copyarray = array.copy()

print('\nOriginal Array = ',array)

array[0] = 11

print('\n Original Array after changes = ',array)

print('\nCopied of Array = ',copyarray)

viewarray = array.view()

print('\nOriginal Array = ',array)

array[0]=20

print('\nOriginal Array after chnges = ',array)

print('\nViewed Array = ',viewarray)

print('\nComplex Array4 = ',array4)

print('\nMatric Array 5 =\n' ,array5)



