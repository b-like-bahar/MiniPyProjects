from tkinter import *
import ast
import math

root = Tk()

index=0
# Insert a number at the current cursor position in the input field
def get_number(num):
    global index
    display.insert(index, num)
    index+=1

# Insert an operator at the current cursor position in the input field and update the index
def get_operator(operator):
    global index
    display.insert(index, operator)
    index+=len(operator)

#cleare everything in input filed
def clear_all():
    display.delete(0,END)

#calculate the calculation in input field
def calculate():
    calculation = display.get()
    try:
        # Replace '√' with 'math.sqrt'
        calculation = calculation.replace("\u221A", "math.sqrt")
        # Replace 'π' with 'math.pi'
        calculation = calculation.replace("\u03C0", "math.pi")
        # Replace '^' with '**'
        calculation = calculation.replace("^", "**")

        node = ast.parse(calculation, mode="eval")
        result = eval(compile(node, "<string", "eval"))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

display = Entry(root)
display.grid(row=1,columnspan=6)

# number buttons
numbers = [1,2,3,4,5,6,7,8,9]
counter1 = 0
for x in range(3):
    for y in range(3):
        num_button = Button(root,text=numbers[counter1], width=2, height=2, command = lambda text=numbers[counter1]:get_number(text))
        num_button.grid(row=x+2, column=y)
        counter1+=1
zero_button = Button(root, text="0", width=2, height=2, command= lambda : get_number(0))
zero_button.grid(row=5, column=1)

#operator buttons
operators = ["+", "-", "*", "/", "%", "^", "\u03C0" , "(", ")", ".", "\u221A"]

counter2 = 0
for x in range(4):
    for y in range(3):
        if counter2<len(operators):
            operator_button = Button(root, text=operators[counter2], width=2, height=2, command = lambda text=operators[counter2] : get_operator(text))
            operator_button.grid(row=x+2, column=y+3)
            counter2+=1

#ClearAll button
ca_button = Button(root, text="AC", width=2, height=2)
ca_button.grid(row=5, column=0)

#ClearAll button
ca_button = Button(root, text="AC", width=2, height=2, command=clear_all)
ca_button.grid(row=5, column=0)

#Equalto button
eq_button = Button(root, text="=", width=2, height=2, command=calculate)
eq_button.grid(row=5, column=2)

root.mainloop()