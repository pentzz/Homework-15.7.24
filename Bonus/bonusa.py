import random
letters: list = ["a", "b", "c"]
word: str = ""
a: int = int(random.randint(6,21))
for i in range(1, a):
    x: int = random.randint(0,2)
    word = word + letters[x]
print(word)