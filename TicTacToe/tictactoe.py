from tkinter import *

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

root.mainloop()