def add(x,y):
    return f" Addition = {x+y}"

def sub(x,y):
    print(f"Substraction = {x-y}")

print("The name is ", __name__)

if __name__ == '__main__':
    print(add(5,6))
    sub(6,7)

'''
Paste below code into new file 

import If_Name_Fun
print(If_Name_Fun.add(5,5)) # It will give add result only
print(If_Name_Fun.sub(10,5)) # it will give sub result as well as "None" word due to print() statement in IF_Nmae_Fun file
'''