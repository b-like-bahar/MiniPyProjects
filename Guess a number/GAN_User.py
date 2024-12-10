import random

def guess_game_user():
    minimum = 1
    maximum = 1000
    feedback = ''
    while True:
        guess_number = random.randint(minimum,maximum)
        feedback = input(f"Is {guess_number} too high (H), too low (L), or correct (C) ?").lower()
        if feedback == 'l':
            minimum = guess_number+1
        elif feedback == 'h':
            maximum = guess_number-1
        else :
            print(f"Yay, the correct number is {guess_number}")
            break
guess_game_user()