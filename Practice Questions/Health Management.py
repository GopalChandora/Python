print("\t--------------------------------------------------")
print("\t\tWelcome to Health Monitoring")
print("\t--------------------------------------------------")


def getdate():
    import datetime
    return datetime.datetime.now()

actionLR = int(input("Enter 1. lock 2. Retrieve : \t"))

if actionLR == 1:
    name = input("Enter name of customer: ")
    name = name.lower()
    
    if name == "gopal":
        actionEF = int(input("Enter 1. Excerice 2.Food: \t"))
        
        if actionEF == 1:
            data = input("Type here\n")
            f = open("GopalExcercise.txt","a")
            f.write(f"{str(getdate())}\t{data}\n")
            f.close()

        elif actionEF == 2:
            data = input("Type here\n")
            f = open("GopalFood.txt","a")
            f.write(f"{str(getdate())}\t{data}\n")
            f.close()

    elif name == "yash":
        actionEF = int(input("Enter 1. Excerice 2.Food: \t"))

        if actionEF == 1:
            data = input("Type here\n")
            f = open("YashExcercise.txt","a")
            f.write(f"{str(getdate())}\t{data}\n")
            f.close()
        elif actionEF == 2:
            data = input("Type here\n")
            f = open("YashFood.txt","a")
            f.write(f"{str(getdate())}\t{data}\n")
            f.close()
    
    elif name == "arvind":
        actionEF = int(input("Enter 1. Excerice 2.Food: \t"))

        if actionEF == 1:
            data = input("Type here\n")
            f = open("ArvindExcercise.txt","a")
            f.write(f"{str(getdate())}\t{data}\n")
            f.close()
        elif actionEF == 2:
            data = input("Type here\n")
            f = open("ArvindFood.txt","a")
            f.write(f"{str(getdate())}\t{data}\n")
            f.close()

elif actionLR == 2:
    name = input("Enter name of customer: ")
    name = name.lower()
    if name == "gopal":
        actionEF = int(input("Enter 1. Excerice 2.Food: \t"))
        
        if actionEF == 1:
            f = open("GopalExcercise.txt","r")
            for i in f:
                print(i,end="")
            f.close()

        elif actionEF == 2:
            f = open("GopalFood.txt","r")
            for i in f:
                print(i,end="")
            f.close()

    elif name == "yash":
        actionEF = int(input("Enter 1. Excerice 2.Food: \t"))

        if actionEF == 1:
            f = open("YashExcercise.txt","r")
            for i in f:
                print(i,end="")
            f.close()
        elif actionEF == 2:
            f = open("YashFood.txt","r")
            for i in f:
                print(i,end="")
            f.close()
    
    elif name == "arvind":
        actionEF = int(input("Enter 1. Excerice 2.Food: \t"))

        if actionEF == 1:
            f = open("ArvindExcercise.txt","r")
            for i in f:
                print(i,end="")
            f.close()
        elif actionEF == 2:
            f = open("ArvindFood.txt","r")
            for i in f:
                print(i,end="")
            f.close()
else:
    print("Invalid Input! Try Again")


'''
class gopal:
    def gopallock(self):
        f = open('Gopallock.txt','w')
        f.close()
    def gopalretrive(self):
        f = open('Gopalretrive.txt','w')
        f.close()

class yash:
    def yashlock(self):
        f = open('Yashlock.txt','w')
        f.close()
    def yashretrive(self):
        f = open('Yashretrive.txt','w')
        f.close()

class arvind:
    def arvindlock(self):
        f = open('Arvindlock.txt','w')
        f.close()
    def arvindretrive(self):
        f = open('Arvindretrive.txt','w')
        f.close()


name = input("Enter name of customer: ")
name = name.lower()

if name.isnumeric():
    raise Exception("Only Charachters are allowed:")

if name == 'gopal':
    action = input("\nEnter 1. Lock 2. Reterive:\t")
    objgopal = gopal()
    if action == 1:
        objgopal.gopallock()
    elif action ==2:
        objgopal.gopalretrive()
    else:
        print("Invalid Input.")
elif name == 'yash':
    action = input("Enter 1. Lock 2. Reterive:\t")
    objyash = yash()
    if action == 1:
        objyash.yashlock()
    elif action == 2:
        objyash.yashretrive()
    else:
        print("Invalid Input.")

elif name == 'arvind':
    action = input("Enter 1. Lock 2. Reterive\t")
    objarvind = arvind()
    if action == 1:
        objarvind.arvindlock()
    elif action == 2:
        objarvind.arvindretrive()
    else:
        print("Invalid Input.")
else:
    print("Invalid customer name! Customer is not in record.")
'''