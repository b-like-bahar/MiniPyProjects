from tkinter import *

def assign_tile(row, column):
    global current_player
    if board[row][column]["text"] !="":
        return

    board[row][column]["text"] = current_player

    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO

    turn_label["text"]= current_player +"'s turn"

def new_game():
    pass

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