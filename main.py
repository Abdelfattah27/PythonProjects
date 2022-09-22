import string
import random
passWord = ""
lowerCase = list(string.ascii_lowercase)
upperCase = list(string.ascii_uppercase)
digit = list(string.digits)
punctuation = list(string.punctuation)
n = 0
while True:
    try:
        n = int(input("Please, Enter the length of the password : "))
        if n > 6:
            break
        else:
            print("the length must be greater than 6 charachers")
    except:
        print("please, Enter integer input")

random.shuffle(upperCase)
random.shuffle(lowerCase)
random.shuffle(digit)
random.shuffle(punctuation)
numOfChars = 0.3 * n
numOfPuncAndDigits = 0.2 * n
for i in range(int(numOfChars)):
    passWord += lowerCase[i]
    passWord += upperCase[i]
for i in range(int(numOfPuncAndDigits)):
    passWord += punctuation[i]
    passWord += digit[i]
while len(passWord) != n:
    passWord += lowerCase[random.randint(0, 25)]

passWord = "".join(random.sample(passWord, n))

print(passWord)