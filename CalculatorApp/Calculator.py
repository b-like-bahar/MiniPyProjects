from tkinter import *

root = Tk()
display = Entry(root)
display.grid(row=1,columnspan=6)

# number buttons
counter1 =1
for x in range(3):
    for y in range(3):
        num_button = Button(root,text=counter1, width=2, height=2)
        num_button.grid(row=x+2, column=y)
        counter1+=1

zero_button = Button(root, text="0", width=2, height=2)
zero_button.grid(row=5, column=1)

#operator buttons
operators = ["+", "-", "x", "/", "%", "^", "\u03C0" , "(", ")", "^2", "\u221A" ]

counter2 = 0
for x in range(4):
    for y in range(3):
        if counter2<len(operators):
            operator_button = Button(root, text=operators[counter2], width=2, height=2)
            operator_button.grid(row=x+2, column=y+3)
            counter2+=1


root.mainloop()