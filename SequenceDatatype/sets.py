clg={"Classroom"," Labs","Canteen","Office"}
print('\n clg :',clg)

print('\n Length :',len(clg))

print('\n Type :',type(clg)) # printing the type 

clg1=clg.copy()
print('\n clg1:',clg1)

print('\n clg1 is subset clg :',clg1.issubset(clg))#issubset

print('\n clg is superset clg1 :',clg1.issuperset(clg))#issuperset

clg.remove("Canteen")# removing element
print('\n Removing :',clg)

print('\n intersection :',clg.intersection(clg1)) #intersection

clg.intersection_update(clg1)
print('\n intersection_update :',clg) #intersection_update

print('\nClg are disjoint to clg1:',clg.isdisjoint(clg1)) #isdisjoint

clg.add("Washroom") # adding element 
print('\n Adding :',clg)

print('\n clg1 is subset clg :',clg1.issubset(clg))#issubset

print('\n clg is superset clg1 :',clg.issuperset(clg1))#issuperset

print('\n Difference clg - clg1 :',clg.difference(clg1)) # difference 

clg.difference_update(clg1) # difference updating 
print('\n difference update  clg - clg1= ',clg)
a = { 1,2,3,4}
b= {2,4,6,8}
a.discard(3) # discard only single element
print('\n Discard :',a)

print('\n A union B :',a.union(b))

b.pop()#poping removing last element 
print('\n pop :',b)
 
print('\n symmetric difference :',a^b)# symmetric difference
a.symmetric_difference_update(b)
print('\n symmetric_difference_update :',a)
clg.clear() # clear the elements in set
print('\n clear :',clg)