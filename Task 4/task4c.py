import random

a: list = []
for i in range(1, 11):
    x: bool = random.choice(["True", "False"])
    a.append(x)
print(a)
