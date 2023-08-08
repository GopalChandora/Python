'''
map function 
map(function,iterable)
https://www.w3schools.com/python/ref_func_map.asp
'''

line = ["1","2","3","4"]

line = list(map(int,line))
for i in range(len(line)):
    line[i] = line[i]*line[i]
print(line)
