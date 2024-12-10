import random

def guess_game():
    goal_number = random.randint(1,20)
    print("Welcome to the guessing a number game (computer version)!")

    while True:
        try:
            guess_number = int(input("Please enter an integer between 1 to 20: "))

            # Check if the number is within the valid range
            if guess_number>20 or guess_number<1:
                print("Invalid input, number should be between 1 and 20. Try again.")
                continue
            # Loop until the correct guess
            while guess_number != goal_number:
                if goal_number > guess_number:
                    guess_number= int(input("Too low, guess again: "))
                else:
                    guess_number= int(input("Too large, guess again: "))
            print(f"Your guess is correct the right number is: {goal_number}")
            break
        except ValueError:
            #Handle inputs that their type is other than integer
            print("Invalid input, please enter an integer. Try again.")
            continue

guess_game()