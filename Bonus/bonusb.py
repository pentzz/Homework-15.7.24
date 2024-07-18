import random
letters: list = ["a", "b", "c"]
words: list = []
number_of_words: int = random.randint(10, 20)
for j in range(0, number_of_words):
    word: str = ""
    a: int = int(random.randint(6, 21))
    for i in range(1, a):
        x: int = random.randint(0, 2)
        word = word + letters[x]
    words.append(word)
print(words)
print(len(words))
