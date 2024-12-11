import random

def rps():
    print("This game is played for 5 repetitions.")

    rps_obj = {
        "r" : 1,
        "p" : 2,
        "s" : 3
    }
    computer_score = 0
    user_score = 0
    counter = 0
    while counter < 5:
        user_input = input("Please choose between rock (r), paper (p),and scissor (s): ").lower()
        computer_choice = random.randint(1,3)

        #When the user choose rock
        if user_input=="r":
            if computer_choice == rps_obj["r"]:
                print("I chose rock, it is a tie")
            if computer_choice == rps_obj["p"]:
                print("I chose paper, I win")
                computer_score+=1
            if computer_choice == rps_obj["s"]:
                print("I chose scissor, you win")
                user_score += 1

        # When the user choose paper
        elif user_input=="p":
            if computer_choice == rps_obj["r"]:
                print("I chose rock, you win")
                user_score += 1
            if computer_choice == rps_obj["p"]:
                print("I chose paper, it's a tie")
            if computer_choice == rps_obj["s"]:
                print("I chose scissor, I win")
                computer_score+=1

        # When the user choose scissors
        elif user_input=="s":
            if computer_choice == rps_obj["r"]:
                print("I chose rock, I win")
                computer_score+=1
            if computer_choice == rps_obj["p"]:
                print("I chose paper, you win")
                user_score += 1
            if computer_choice == rps_obj["s"]:
                print("I chose scissor, it's a tie")
        # When the user input is invalid
        else:
            print("Your input is invalid! Try again.")
            continue

        counter+=1

    #Final results
    if computer_score > user_score :
        print("Game over! Here are the final results:")
    elif computer_score < user_score :
        print("Congrats you won! Here are the final results:")
    else:
        print("It is a tie! Here are the final results:")
    print(f"Computer score: {computer_score}\nUser score: {user_score}")
rps()