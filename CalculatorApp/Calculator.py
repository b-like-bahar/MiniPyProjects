from tkinter import *

root = Tk()
display = Entry(root)
display.grid(row=1,columnspan=6)

counter =1
for x in range(3):
    for y in range(3):
        num_button = Button(root,text=counter, width=2, height=2)
        num_button.grid(row=x+2, column=y)
        # num_button.pack()
        counter+=1

zero_button = Button(root, text="0", width=2, height=2)
zero_button.grid(row=5, column=1)
root.mainloop()