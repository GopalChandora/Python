apple = int(input("Enter number of apples : \t"))
minvalue = int(input("Enter Minimum range value : \t"))
maxvalue = int(input("Enter Maxmimum range value : \t"))

if minvalue>maxvalue:
    print("Oh no ! Invalid input as maximum value is less than minimum value")

elif(minvalue == maxvalue):
    print("Oh no ! Invalid input both values are equal")

else:
    for i in range(minvalue,maxvalue+1):
        if apple % i == 0:
            print(i,"is a divisor of ",apple)
        else:
            print(i,"is a not divisor of ",apple)
