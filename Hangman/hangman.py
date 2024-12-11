import random
from words import words
import string

print("Welcome to the Hangman game, you have 7 lives")

# Prevent selecting a word with "-" or space in the middle
def valid_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

#live counter
def live_counter(live):
    if live==1:
        print(f"You have {live} live")
    else:
        print(f"You have {live} lives")

def hangman():
    word=valid_word()
    word_letters=set(word.upper())
    used_letters=set()
    alphabet_letters=set(string.ascii_letters)
    live = 7

    while len(word_letters) > 0 and live > 0:
        #current state of the word like W-RD
        word_list = [letter if letter in used_letters else "-" for letter in word]
        live_counter(live)
        print("You have already used: ", ", ".join(used_letters))
        print("Current word is: "," ".join(word_list))
        user_input= input("Please enter a letter: ").upper()
        if user_input in alphabet_letters - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                live-=1
        elif user_input in used_letters:
            print("You have already used this letter. Try again!")
        else:
            print("The input is invalid. Try again!")

    if live==0:
        print(f"Game over! The word is {word}")
    else:
        print(f"Yay, you guessed correct. The word is {word}")

hangman()