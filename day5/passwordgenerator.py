import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def random_letter():
    # return letters[random.randint(0,len(letters)-1)]
    return random.choice(letters)

def random_number():
    # return numbers[random.randint(0,len(numbers)-1)]
    return random.choice(numbers)

def random_symbol():
    # return symbols[random.randint(0,len(symbols)-1)]
    return random.choice(symbols)

def random_item_type_order():
    itemTypes = ["letters","numbers","symbols"]
    random.shuffle(itemTypes) 
    return itemTypes

print("Welcome to the PyPassword Generator")
numOfLetters = int(input("How many letters in the password? "))
numOfNumbers = int(input("How many numerals in the password? "))
numOfSymbols = int(input("How many symbols in the password? "))

passwordAsList = []
for index in range(0,numOfLetters):
    passwordAsList.append(random_letter())

for index in range(0,numOfNumbers):
    passwordAsList.append(random_number())

for index in range(0,numOfSymbols):
    passwordAsList.append(random_symbol())

random.shuffle(passwordAsList)
print(len(passwordAsList))

password = ""
for item in passwordAsList:
    password += item

print(f"password = {password}")


