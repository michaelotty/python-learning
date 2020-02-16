from random import random

a = [0, 0, 0, 0, 0]

for i in range(5):
    a[i] = random()

print(a)

b = [random() for i in range(5)]
print(b)
