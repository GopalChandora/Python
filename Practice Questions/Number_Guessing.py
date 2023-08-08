print("\t----------------------------------------------------")
print("\t\tWelcome to The Number Guessing Game")
print("\t\tYou have 5 chances to guess the number:")
print("\t----------------------------------------------------")

actualnum = 15
count = 1
while count<=5:
    usernum = int(input("\nEnter a number: "))
    if usernum > actualnum:
        print("Enter lower number")
        # count-=1
        # print("No of guess remaining =",count)
            
    elif usernum == actualnum:
        print("*** Hurray! You Won ***")
        print(f"You guesses the correct number {actualnum} in {count} count")
        break

    else:
        print("Enter higher number")
        # count-=1
        # print("No of guess remaining =",count)
    print("No of chances left",5-count)
    count+=1

if count > 5:
        print("\nGame Over")
        print("Your Ran out of chance")
       