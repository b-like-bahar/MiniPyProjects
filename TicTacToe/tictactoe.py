from tkinter import *

def assign_tile(row, column):
    global current_player

    if game_finished == True:
        return

    if board[row][column]["text"] !="":
        return

    board[row][column]["text"] = current_player

    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO

    turn_label["text"]= current_player +"'s turn"

    winner_detector()

def winner_detector():
    global turns, game_finished
    turns+=1

    #check winner horizontally
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != "":
            turn_label.config(text=f"{board[row][0]['text']} is winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_finished=True
            return

    # check winner vertically
    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] !="":
            turn_label.config(text=f"{board[0][column]['text']} is winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_finished=True
            return

    # check winner diagonally
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "":
        turn_label.config(text=f"{board[0][0]['text']} is winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_finished=True
        return

    # check winner anit-diagonally
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "":
        turn_label.config(text=f"{board[0][0]['text']} is winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_finished=True
        return

    # tie
    if turns == 9:
        turn_label.config(text="Tie!", foreground=color_yellow)
        game_finished = True
        return

def new_game():
    global turns, game_finished
    turns = 0
    game_finished = False
    turn_label.config(text=f"{current_player}'s turn", foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

#game setup
playerX = "X"
playerO = "O"
current_player = playerX
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"
turns = 0
game_finished = False

# main window setup
root = Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

frame = Frame(root)
frame.pack()

turn_label = Label(frame, text=f"{current_player}'s turn", font=("Helvetica", 20), bg=color_gray, fg="white")
turn_label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame, text="", font=("Helvetica", 20, "bold"),
                                    background=color_gray, foreground=color_blue, width=4, height=3,
                                    command = lambda row=row, column=column: assign_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

restart_btn = Button(frame, text=f"restart", font=("Helvetica", 20), bg=color_gray, fg="white", command=new_game)
restart_btn.grid(row=4, column=0, columnspan=3, sticky="we" )


root.mainloop()