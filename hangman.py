# Step 1

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
maharshi = []

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
chosen_word = random.choice(word_list)
y = []
for x in chosen_word:
    y.append(x)

for x in range(len(chosen_word)):
    maharshi += "_"
print(maharshi)
m = 0

endgame = False
while not endgame:
    maggy = str(input("guess a letter  "))

    count = 0
    for x in chosen_word:

        if x == maggy:
            maharshi[count] = x
        if maggy not in y:
            m+=1

        count += 1
    print(maharshi)
    t=int(m/len(chosen_word))
    print(stages[6-t])
    if t==6:
        print("you lost")
        break

    if "_" not in maharshi:
        endgame = True
        print("You win")