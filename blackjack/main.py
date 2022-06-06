import random
import art
print(art.logo)
cards = [11, 2, 3, 4, 5, 5, 7, 8, 9, 10]


def shri():
    m = []
    a = [random.choice(cards)]

    m.append(random.choice(cards))
    maggy = False
    while not maggy:

        m.append(random.choice(cards))

        print(f"your cards {m} {sum(m)}")
        print(f"Computer card is{a}")
        if input('enter "y" to get another card or "n"') == "n":
            maggy = True
        if 11 in m and sum(m) > 21:
            s = m.index(11)

            m[s] = 1

    maharshi = False
    while not maharshi:
        if 11 in a and sum(a) > 21:
            h = a.index(11)
            a[h] = 1

        if sum(a) < 17:
            a.append(random.choice(cards))
        else:
            maharshi = True

    print(f"computer cards{a} {sum(a)}")

    if sum(m) > 21 and sum(a) > 21 or sum(a) == sum(m):
        print("Draw")
    elif sum(a) > 21:
        print("you win")
    elif sum(m) > 21:
        print("you lose")
    elif sum(m) > sum(a):
        print("you win")
    else:
        print('you lose')
    if input("enter 'y' to play again 'n' to exit") == 'y':
        shri()


shri()
