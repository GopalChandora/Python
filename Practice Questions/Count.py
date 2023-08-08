num=(1,2,3,4,5,6,7,8,9)
print('numbers =',num)
count_even=0
count_odd =0
for i in num :
    if i % 2 :
        count_even+=1
    else :
        count_odd+=1
print(' Counts of even number :',count_even)
print(' Counts of odd number :',count_odd)