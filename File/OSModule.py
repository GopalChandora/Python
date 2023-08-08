# os Module
''' Used to establish the interaction between the user and the operating system.
 Offers many useful OS functions that are used to perform OS-based tasks
 To get related information about operating system           '''

import os  # importing module to use functions available in it

#methode 1
os.name()
print(os.name)
''' Provides the name of the operating system module that it imports  '''

#Method 2
os.rename()         
os.rename("abc.txt", "hello.txt")
#To rename the file 

#Method 3
os.getcwd()         
print(os.getcwd())
#To get current working directory

#Method 4
os.chdir()       
os.chdir("Extc")
#To chnage the current working directory 

os.chdir("C:\\Users\\Admin\\Desktop")

#Method 5
os.mkdir()
os.mkdir("Terna")
''' To create new directory in current working directory   '''

#Method 6
os.mkdir("d:\\Terna")
''' To create new directory to the specidfied path '''

#Method 7
os.rmdir()
''' To remove the directory specified in path
First, we have to change the current working directory and remove the folder   '''
os.rmdir("Terna")

#Method 8
os.remove()         
os.remove("C:\\Users\\Admin\\Desktop\\Terna\\hello.txt")
#To remove file specified in path

#Method 9
os.error() 
import os

try:
    f = open("python.txt", 'r')
    print(f.read())
    f.close()

except IOError:
    print("File Doesnt Exist !!")
        
''' Defines the OS level errors
It raises OSError in case of invalid or inaccessible file names and path  '''

#method 10
# os.popen(file_name,mode)
''' used to open a file in OS module'''

#Method 11
os.closed()
''' used to closed a file opened by os.popen() only in OS module'''





