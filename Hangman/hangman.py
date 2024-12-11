import random
from words import words

print("Welcome to the Hangman game, you have 6 lives")

# Prevent selecting a word with "-" or space in the middle
def valid_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = words.random.choice(words)
    return word.uppercase()