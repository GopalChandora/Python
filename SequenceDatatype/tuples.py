''' Tuple separated by (,) then it is tuple,if not the it will become string '''
t1=( "GOPAL","EXTC",4) # created tuple
t2=("E","N","G","I","N","E","E","R","I","N","G")

print(t1,'\n',t2) 

print('\n Length :',len(t2)) # printing length of tuple

print('\n Type :',type(t1)) # printing the type of t1

print(id(t1))
print(id(t2))

print(( "E","X","T","C") + ("S","E","M",4))# Concatinating

print(("G","O","P","A","L")*3)# Multiple printing

print(t1[1:2]) # positive slicing 
print(t1[-2:-1]) # negative slicing

(name,branch,sem) = t1 #unpacking of tuple 
print('\n Name :',name)
print('\n Branch :',branch)
print('\n Sem :',sem)

count = t2.count('E') # Counting the letter 
print('\n Count : ',count)

print('\n Index ',t2[4]) # printing the value present at index 4