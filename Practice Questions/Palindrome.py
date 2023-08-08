num = input("enter a number")
num_copy = str(num)
temp = ""
for i in num_copy:
    temp = i+temp
if temp == num_copy:
    print("palindrome")
else:
    print("not palindrome")

'''
# Palindrome And Symmertical

def palindrome(line):
    temp = ""

    for i in line:
        temp = i+temp

    if temp == line:
        print("Palindrome")
    else:
        print("Not Palindrome")

def symmertical(line): #nitin
    mid = int(len(line)//2) # 5//2 = 2

    if len(line)%2 == 0: # 5 % 2 == 0 (No) 
        first_half = line[:mid]
        second_half = line[mid:]
    else:
        first_half = line[:mid] # line = ni [0,1]
        second_half = line[mid+1:] # line = [3,4]

    if first_half == second_half:
        print("Symmetrical")
    else:
        print("Not Symmertrical")

line = input()
palindrome(line)
symmertical(line)'''

    