pos: int = 0
neg: int = 0
z: int = 0
ln: int = None
lp: int = None
sev: int = 0
for i in range(1, 11):
    num: int = int(input("Please enter a number: "))
    if num > 1000 or num < -1000:
        continue
    if num == -999:
        break
    z = z + 1 if num == 0 else z
    sev = sev + 1 if num % 7 == 0 and num != 0 else sev
    pos = pos + 1 if num > 0 else pos
    neg = neg + 1 if num < 0 else neg
    ln = num if num <= 0 and num != 0 else ln
    lp = num if num >= 0 and num != 0 else lp
else:
    print(f"The count of positive numbers is: {pos}\nThe count of negative numbers is: {neg}"
          f"\nThe count of numbers divided by 7 is: {sev}\nThe count of zero is: {z}")
    print(f"The last positive number is: {lp}\nThe last negative number is:{ln}")
