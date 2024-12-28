from tkinter import *

game_width = 700
game_height = 700
speed = 50
space_size = 50
body_pats = 2

#colors
snake_color = "#4584b6"
food_color = "#ffde57"
background_color = "000000"



# main window setup
root = Tk()
root.title("Snake Game")
root.resizable(False, False)

score = 0
direction="down"

score_label = Label(text="score:{}".format(score), font=("Helvetica", 20))
score_label.pack()


root.mainloop()