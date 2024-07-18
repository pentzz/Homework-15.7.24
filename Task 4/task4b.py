import random

a: list = []
for i in range(1, 11):
    x: int = random.randint(1, 9999)
    a.append(x)
print(a)
