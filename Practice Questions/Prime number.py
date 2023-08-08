num = int(input("Enter a number to check is it prime or not"))
if num > 1:
    for i in range(2,int(num/2)+1):
        if (num%i)==0:
            print("is not prime ")
            break
    else:
        print("is Prime number")
else:
    print("number is not prime")

'''
# Python program to print all
# prime number in an interval
 
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                print(j)
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 
# Driver program
starting_range = 0
ending_range = 10
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
'''