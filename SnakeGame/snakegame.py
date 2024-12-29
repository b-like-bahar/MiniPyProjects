from pty import spawn
from tkinter import *
import random

class Food:
    def __init__(self):
        x = random.randint(0, (game_width / space_size)-1) * space_size
        y = random.randint(0, (game_height / space_size) - 1) * space_size

        self.coordinate = [x,y]
        canvas.create_oval(x, y, x+space_size, y+space_size, fill=food_color)

class Snake:
    def __init__(self):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        for i in range(0, body_parts):
            self.coordinates.append([0, 0])

        for x,y in self.coordinates:
            squares = canvas.create_rectangle(x, y, x+space_size, y+space_size, fill=snake_color)
            self.squares.append(squares)

def next_turn(snake, food):
    x,y=snake.coordinates[0]

    if direction == "up":
        y -=space_size
    elif direction == "down":
        y += space_size
    elif direction == "left":
        x -= space_size
    elif direction == "right":
        x += space_size

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x+space_size, y+space_size, fill=snake_color)
    snake.squares.insert(0, square)
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

    root.after(speed, next_turn, snake, food)



game_width = 700
game_height = 700
speed = 50
space_size = 50
body_parts = 2

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
snake = Snake()
next_turn(snake, food)

root.mainloop()