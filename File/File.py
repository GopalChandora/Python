with open("xyz.txt",'r') as f: # if we open a file by "with" no need to close file 

# f = open("xyz.txt","r")
    print("file pointer",f.tell()) # tell function used to get the file pointer position
    print(f.readline())
    print("file pointer",f.tell())
    print(f.seek(5)) # seek function used to set the file pointer position
    print("file pointer",f.tell())
    print(f.readline())
    print("file pointer",f.tell())
# f.close

# we can use a file outside a file
# f = open("xyz.txt","r")
# print("out",f.read())
# f.close

