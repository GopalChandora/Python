# VCDS (Vowels, consonant,digi,special characters)
data = input("Enter a String:")
vowels = 0
consonant = 0
digit = 0
special = 0

for i in data:
# for x in range(len(data)):
#     i = data[x]
    if i >='a' and i <='z' or i>='A' and i<='Z':
        i = i.lower()
        if i == 'a' or i == "e" or i == 'i' or i == "o" or i == 'u':
            vowels+=1
        else:
            consonant+=1
    elif i >= '0' and i <= '9':
        digit+=1
    else:
        special+=1
print(f" Vowels = {vowels}\n Consonant = {consonant}\n Digits = {digit}\n Special = {special}")