# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)


# n = int(input("Enter a number: "))
n = []
for i in range(1500,2700):
    if i%7==0 and i%5==0:
        # print(i,end = " ")
        n.append(str(i))
print(n)
# print(', '.join(n))