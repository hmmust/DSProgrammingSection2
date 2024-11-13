from numpy import random
import numpy as np
import string

chars= list(string.ascii_letters)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

print("".join(random.choice(chars,5)))
