x = 25
y = 3.1416
z = 25j

print(type(x))
print(type(y))
print(type(z))

# now we convert the the types

a = float(x)
b = int(y)

print(type(a))
print(type(b))

# Random Number
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random
print(random.randrange(1,100))
