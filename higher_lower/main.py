import random
import game_data
import art
print(art.logo)
a = random.choice(game_data.data)


count=0


correct = True
while  correct:
    b = random.choice(game_data.data)
    d=a['follower_count']
    e=b['follower_count']
    print(f"{a['name']} is a {a['description']} from {a['country']}")
    print(art.vs)
    print(f"{b['name']} is a {b['description']} from {b['country']}")
    if d > e:
        if 'a' == input("enter 'a' or 'b "):
            count=count+1
            a = b
           
        else:
            print(f"Sorry You entered wrong option your score is {count}")
            correct = False
    if e > d:
        if 'b'== input("enter 'a' or 'b "):
            count=count+1
            a = b

        else:
            print(f"Sorry You entered wrong option your score is {count}")
            correct = False

