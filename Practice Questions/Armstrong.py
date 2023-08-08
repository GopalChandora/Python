num = int(input("Enter a number"))
sum =0
temp = num
while num>0:
    rem = num%10
    sum = sum+(rem**3)
    num = num//10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")