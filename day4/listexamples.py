import random

# Data Structures Doc : https://docs.python.org/3/tutorial/datastructures.html

# Input as string w/ comma separator
inputNames = input("Provide comma separated list of participants. ")
names = inputNames.split(",")
print(names)

# Clean up names by removing whitespace
strippedNames = []
for name in names:
    strippedNames.append(name.strip())

numberOfNames = len(strippedNames)
print(numberOfNames)
print(strippedNames)

# Choose one person randomly to pay for lunch
payeeIndex = random.randint(0,numberOfNames-1)
print(f"{strippedNames[payeeIndex]} has to pay the bill!!")
print(f"(using choice) {random.choice(strippedNames)} has to pay the bill!!")