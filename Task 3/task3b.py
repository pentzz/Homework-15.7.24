while True:
    num: int = int(input("Please enter a number: "))
    if num % 2 == 0 and num > 0:
        continue
    else:
        break
space: int = num - 2
for i in range(1, num+1, 2):
    print(" " * space, end="*" * i)
    print()
    space -= 1
