#!/bin/python

from tkinter import *

# renaldi was here

inputs = []

def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	inputs.clear()
	e.delete(0, END)

def button_operate(operation):
	global inputs

	currNum = e.get()
	e.delete(0, END)

	if (operation != "="):
		inputs.append(int(currNum))
		inputs.append(operation)
	else:
		inputs.append(int(currNum))
		e.insert(0, calculate())

def calculate():
	ans = inputs[0]
	operation = inputs[1]
	for i in range(2, len(inputs)):
		if i % 2 == 0:
			number = inputs[i]
			if operation == "+":
				ans += number
			elif operation == "-":
				ans -= number
			elif operation == "/":
				ans /= number
			elif operation == "*":
				ans *= number
		else:
			operation = inputs[i]

	return ans

def validate(P):
	if str.isdigit(P) or P == "":
		return True
	else:
		return False

# Initial
root = Tk()
root.title("Simple Calculator")

# Define Entry
vcmd = root.register(validate)
e = Entry(root, width=35, borderwidth=5, validate="all", validatecommand=(vcmd, "%P"))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define Buttons
button_1 = Button(root, text="1", width=10, height=5, command=lambda: button_click(1))
button_2 = Button(root, text="2", width=10, height=5, command=lambda: button_click(2))
button_3 = Button(root, text="3", width=10, height=5, command=lambda: button_click(3))
button_4 = Button(root, text="4", width=10, height=5, command=lambda: button_click(4))
button_5 = Button(root, text="5", width=10, height=5, command=lambda: button_click(5))
button_6 = Button(root, text="6", width=10, height=5, command=lambda: button_click(6))
button_7 = Button(root, text="7", width=10, height=5, command=lambda: button_click(7))
button_8 = Button(root, text="8", width=10, height=5, command=lambda: button_click(8))
button_9 = Button(root, text="9", width=10, height=5, command=lambda: button_click(9))
button_0 = Button(root, text="0", width=10, height=5, command=lambda: button_click(0))

button_add = Button(root, text="+", width=10, height=5, command=lambda: button_operate("+"))
button_subtract = Button(root, text="-", width=10, height=5, command=lambda: button_operate("-"))
button_multiply = Button(root, text="*", width=10, height=5, command=lambda: button_operate("*"))
button_divide = Button(root, text="/", width=10, height=5, command=lambda: button_operate("/"))
button_equal = Button(root, text="=", width=10, height=5, command=lambda: button_operate("="))
button_clear = Button(root, text="Clear", width=10, height=5, command=button_clear)

# Put the buttons on the screen

button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_clear.grid(row=4, column=1)
button_0.grid(row=4, column=2)
button_equal.grid(row=4, column=3)

button_add.grid(row=1, column=0)
button_subtract.grid(row=2, column=0)
button_multiply.grid(row=3, column=0)
button_divide.grid(row=4, column=0)

root.mainloop()