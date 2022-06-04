# Step 1

import random
import hangman_art
import hangman_word



maharshi = []
y=[]

print("Wel-come to ")
print(hangman_art.logo)
print("game\n")
chosen_word = random.choice(hangman_word.word_list)



for x in range(len(chosen_word)):
 maharshi += "_"
print(maharshi)
m = 0

endgame = False
while not endgame:
    maggy = str(input("guess a letter  "))
    y.append(maggy)
    print(y)
    
    if maggy in maharshi:
        print("you already entered the letter")
        

    count = 0
    for x in chosen_word:

        if x == maggy:
            maharshi[count] = x
        if maggy not in chosen_word:
            m+=1
            

        count += 1
    print(maharshi)
    t=int(m/len(chosen_word))
    print(hangman_art.stages[6-t])
    if t==6:
        print("you lost")
        print(chosen_word)
        break

    if "_" not in maharshi:
        endgame = True
        print("You win")