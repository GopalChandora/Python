birthdate = input("Enter your Age or Birth Year : \t")
period_age_year = input("Enter age or year to find what will be the year or age at that peroid : ")

def Find_Year(actual_age,period_age):
    current_year = int(input("Enter current year : \t"))
    # result_birth_year = current_year - int(actual_age)
    # result_period_year = result_birth_year + int(period_age)
    # print("you will be",period_age,"yrs old in the year ", result_period_year)

    difference_age = int(period_age) - int(actual_age)
    result_period_year = int(current_year) + int(difference_age)
    print("At age of",period_age, "yrs the year will be ", result_period_year)

def Find_age(actual_year,period_year):
    result_period_age = int(period_year) - int(actual_year)
    print("In",period_year, " you will be",result_period_age," yrs old")


if len(birthdate) == 2 and len(period_age_year) == 2:
    Find_Year(birthdate,period_age_year)

elif len(birthdate) == 2 and len(period_age_year) == 4:
    current_year = int(input("Enter current year : \t"))
    difference_year = int(period_age_year) - int(current_year)
    result_age = int(birthdate) + int(difference_year)
    print("you will be",result_age,"yrs old in ",period_age_year,)
    
elif len(birthdate) == 4 and len(period_age_year) == 2:
    result_year = int(birthdate) + int(period_age_year)
    print("when you are ",period_age_year,"yrs old The year will be",result_year)

elif len(birthdate) == 4 and len(period_age_year) == 4:
    Find_age(birthdate,period_age_year)
    
else:
    print("Oh no! Invalid Input please check and try again")

'''
#  For getting year at which user will turn 100 yrs old
birthdate = input("Enter your Age or Birth Year : \t")

if len(birthdate) == 2:
    current_year = int(input("Enter current year : \t"))
    result_age = current_year - int(birthdate)
    print("You will be 100yrs old in ",result_age+100)

elif len(birthdate) == 4:
    result_year = int(birthdate) + 100
    print("You will be 100yrs old in ",result_year)
    # print("You will be 100yrs old in ",int(birthdate)+100)

else:
    print("Oh no! Invalid Input check and try again")

'''

'''
# USING FUNCTION For getting year at which user will turn 100 yrs old 
def result_print(result):
    print("You will be 100yrs old in ",result+100)

birthdate = input("Enter your Age or Birth Year : \t")

if len(birthdate) == 2:
    current_year = int(input("Enter current year : \t"))
    result_age = (current_year - int(birthdate))+100
    result_print(result_age)
    # print("You will be 100yrs old in ",result+100)

elif len(birthdate) == 4:
    result_year = int(birthdate) + 100
    result_print(result_year)
    # print("You will be 100yrs old in ",result)
    # print("You will be 100yrs old in ",int(birthdate)+100)

else:
    print("Oh no! Invalid Input check and try again")
'''