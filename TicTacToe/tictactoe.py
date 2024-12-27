from tkinter import *

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
root.title = ("Tic Tac Toe")
root.resizable(False, False)

frame = Frame(root)
frame.pack()

turn_label = Label(frame, text=f"{current_player}'s turn", font=("Helvetica", 20), bg=color_gray, fg="white")
turn_label.grid(row=0, column=0, columnspan=3, sticky="we")

restart_btn = Button(frame, text=f"restart", font=("Helvetica", 20), bg=color_gray, fg="white", command=new_game)
restart_btn.grid(row=4, column=0, columnspan=3, sticky="we" )
root.mainloop()