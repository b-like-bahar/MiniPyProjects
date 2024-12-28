from pty import spawn
from tkinter import *
import random

class Food:
    def __init__(self):
        x = random.randint(0, (game_width / space_size)-1) * space_size
        y = random.randint(0, (game_height / space_size) - 1) * space_size

        self.coordinate = [x,y]
        canvas.create_oval(x,y,x+space_size, y+space_size, fill=food_color)




game_width = 700
game_height = 700
speed = 50
space_size = 50
body_pats = 2

#colors
snake_color = "#4584b6"
food_color = "#ffde57"
background_color = "#000000"



# main window setup
root = Tk()
root.title("Snake Game")
root.resizable(False, False)

score = 0
direction="down"

score_label = Label(text="score : {}".format(score), font=("Helvetica", 20))
score_label.pack()

canvas = Canvas(root, bg=background_color, height=game_height, width=game_width)
canvas.pack()

food = Food()
root.mainloop()