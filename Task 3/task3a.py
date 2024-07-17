num: int = int(input("Please enter a number: "))
for i in range(1, num+1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    if i == num:
        for k in range(num, 1, -1):
            for h in range(1, k):
                print(h, end="")
            print()