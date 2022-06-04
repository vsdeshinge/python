alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']



def maharshi(m, a,g):
    end_text = ""
    if g == "decode":
        a *= -1
    for char in m:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + a
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {g}d result: {end_text}")
from art import logo
print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the  shift number:\n"))
    shift=shift%26
    maharshi(m=text, a=shift, g=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")