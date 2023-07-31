# Check the Mersenne Twister - used by Python for randomness
# Khan Academy : Pseudo Random Number Generators - https://www.youtube.com/watch?v=GtOt7EBNEwQ
# Ask Python : https://www.askpython.com/python-modules/python-randint-method
import random

# Generate floating point random number between 0 and 5
randomMultiplier = random.randint(0,5)
randomBase = random.random()
print(randomMultiplier * randomBase)