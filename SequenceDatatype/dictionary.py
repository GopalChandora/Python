cars = {1:"BMW",2:"Mercedes",3:"Ferrari",4:"Range rower",5:"Audi"}

print(cars)

print('\n Length :',len(cars)) # calculating length

print(type(cars)) # printing type
 
print(id(cars))

print(cars.get(2))

print(cars.fromkeys(cars,'gopal'))

x = cars.keys()  # keys
print(x) # printing keys

y = cars.items() # items
print(y)# printing items

print(cars[1])

cars1= cars.copy()
print('\n Copy :',cars1)

cars['6']='Lamborgini' # Adding items
print('\n Adding :',cars)

cars[6]='Porche' # Updating value 
print('\n Update :',cars)

print('\n Removing by keys :',cars.pop(3))

print('\n Removing by items :',cars.popitem())

y = cars.setdefault(6,'Aulto')
print(y) # Returns the value of the specified key. If the key does not exist: insert the key, with the specified value


print('\n After removing :',cars)

print('\n gatting value :',5,cars.get(5)) # get

print('\n getting provided value :',6,cars.get(6,'SUV')) # get by providing value

cars.clear() # clear items from dictionary 
print('\n clear :',cars)

cars.update({'name':'gopal'})
print(cars)

del cars
print('cars1 dictionary',cars1)

z = cars1.values()
print(z)