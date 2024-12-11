import random
from words import words
import string

print("Welcome to the Hangman game, you have 6 lives")

# Prevent selecting a word with "-" or space in the middle
def valid_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word=valid_word()
    word_letters=set(word.upper())
    used_letters=set()
    alphabet_letters=set(string.ascii_letters)

    while len(word_letters) > 0 :
        #current state of the word like W-RD
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("You have already used: ", ", ".join(used_letters))
        print("Current word is: "," ".join(word_list))
        user_input= input("Please enter a letter: ").upper()
        if user_input in alphabet_letters - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
        elif user_input in used_letters:
            print("You have already used this letter. Try again!")
        else:
            print("The input is invalid. Try again!")
    print(f"Yay, you guessed correct. The word is {word}")

hangman()