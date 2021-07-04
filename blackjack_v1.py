import random

lt = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, 14]


xlist = []

while True:
    x = random.choice(lt)
    print(x)
    xlist.append(x)
    print("the total is", sum(xlist))

    if sum(xlist) < 21:
        xcont = input("Do you want to continue?")
        if xcont == "y":
            continue
        elif xcont == "n":
            print("Stopped at ", sum(xlist))
            break

        continue
    elif sum(xlist) == 21:
        print("Blackjack!")
    elif sum(xlist) > 21:
        print("Game Over!")
    break
