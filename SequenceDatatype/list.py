''' Syntax : 
name =[]
1. list is enclosed by square bracket [ ] and data is sepreted by (,)
2. we can add alphabets and number in list'''

list = [' aaa ',' bbb ',' ccc',' ddd ',' eee ',' fff ',' ggg ',' hhh ']
list1 = [' yyy ',' zzz ']
print(list)
print(list1)

#type()
print(type(list))

#id()
print(id(list))

#len()
print(len(list))

#slicing
print(list[2]) #Positive
print(list[-2]) #Negative


print(list[1:3]) #Two index
print(list[-3:-1]) #search will start with -3 go till the -1 but -1 will not considered


print(list[:5]) # start with 0 go till 5 but not considering 5 '''
print(list [1:])# start with 1 go till the end. '''


list[7]=' iii ' # replacing hhh to iii 
print(list) 

list[6:7]=' jjj ' 
print(list) #j is divided into three part and iii remain same 
list[6:7]=' j '
print(list) #single j will be replaced by ggg


list.append('ddd')
print(list) #append() it will take only one value and add new value at the end


list.extend(list1)
print(list) #To add or combine a list use extend()


list.remove(' yyy ')
print(list) #To remove we have to specifiy actual value.


list.pop(1)
print(list) #pop() it will remove elements by taking one index value
list.pop( -1)
print(list)


del list[0]
print(list) #delete the element which the user want to by giving the index number and if user not provided any number then the whole list will deleted '''

# list.clear(  ) #clear method empty the list but list will remain without any content in it.


list.insert(4,' sss ')
print(list) #insert a new value without replacing any existing value, a new element will be inserted before the present element and remaining elements index will be +1 by their old index number given by user


list.sort()
print(list) #sorting means aaranging the element in accending order if the first two letter of  element then it will compare the second letter of the both element

list.reverse()
print(list) #reverse the specified list

list2=list.copy()
print(list2) # copying the list to new list
