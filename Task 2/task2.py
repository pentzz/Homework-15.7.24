import random
while True:
    num: int = random.randint(1, 101)
    tries: int = 0
    while True:
        user_num: int = int(input("Please guess the number: "))
        tries += 1
        if user_num == num:
            print(f"B.I.N.G.O")
            break
        if user_num > num:
            print("Your number is too big. Try again..")
            continue
        if user_num < num:
            print("Your number is too small. Try again..")
            continue
    again: str = input(f"Game over!\nThe number of tries was {tries} \nDo you want to play again? (yes/no) ")
    if again == "yes":
        continue
    else:
        break
