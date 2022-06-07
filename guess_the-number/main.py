import random

total_numbers = []
for x in range(1, 101):
    total_numbers.append(x)
chosen_number = random.choice(total_numbers)
level_of_game = input("enter game mode 'hard' or 'easy'")
count = 0
run_loop = False
while not run_loop:
    user_entry = int(input("enter a number"))
    if user_entry == chosen_number:
        print("You win")
        run_loop = True
        break
    elif user_entry < chosen_number - 20:
        print("too low")
    elif user_entry < chosen_number - 5:
        print("low")
    elif user_entry > chosen_number + 20:
        print("too high")
    elif user_entry > chosen_number + 5:
        print("high")
    else:
        print("too close")
    count += 1
    if level_of_game== "hard":
        print(f"remaining attempts {6-count}")
    else:
        print(f"remaining attempts {10 - count}")

    if count == 6 and level_of_game == "hard":
        print(f"you lost, the number is {chosen_number}")
        run_loop = True
    if count == 10 and level_of_game == "easy":
        print(f"you lost, the number is {chosen_number}")
        run_loop = True
