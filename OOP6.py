###Problem 6\

import random
print(random.random())
x = []
for i in range(0, 5):
    if random.random() > 0.1:
        x.append(random.random())
print(x)

##print a random whole Number between 0 to 10.
print(random.randrange(0, 15))

##print a random floating point number between 0 and 10.
print(random.uniform(0, 10))