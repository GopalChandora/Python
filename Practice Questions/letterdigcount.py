def count_letter(word):
    temp = 0
    sum = 0
    for i in word:
        if i.isalpha():
            temp += 1
        elif i.isdigit():
            sum += 1
    print("No. of letters in string : ",temp)
    print("No. of letters in string : ", sum)
    dict.update({"LETTER":temp , "Digits":sum})
    print(dict)

word = input("Enter a string : ")
dict = {}
count_letter(word)