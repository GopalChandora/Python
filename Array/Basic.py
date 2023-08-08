from array import *

sum1=0

v = [1,2,3]
print(sum(v))

val = array('i',[1,2,3])
# newval = array(val.typecode,(i for i in val))

print(type(val))
for i in range(len(val)):
	print(val[i])

for j in range(3):
	sum1+= val[j]
print("sum =", sum1)


print(val.buffer_info()) #(address,size)(2042625868464, 3)