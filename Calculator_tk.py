import tkinter as tk
import tkinter.font

window = tk.Tk()
window.title("Calculator")
window.eval('tk::PlaceWindow . center')
text = tk.StringVar()
text.set('')
display = tk.Entry(window, textvariable = text)
display.grid(row=0, column=0, sticky='nsew',columnspan=4)
display.config(state='readonly')


####

# Creating the Enum of possible actions
# through which we will keep track what
# to do when a new action is used.
from enum import Enum
Action = Enum('Action', ['PLU', 'MIN', 'TIM', 'DIV', 'CLE', 'EQU'])

####

action = Action.PLU
canAction = False
val = 0

####

# Creating a function that will handle what a button
# push should do, so that we can add complexity easier
# later on.

def numberButton(x, text):
    global canAction
    if (canAction):
        text.set(text.get() + x)
    else:
        text.set('')
        text.set(x)
        canAction = True

####

# Creating and setting the number buttons for the calculator

buttons = []
for i in range(10):
    button = tk.Button(window, text=str(i), command=lambda i=i: numberButton(str(i), text))
    if(i != 0):
        button.grid(row=1 + (i - 1) // 3, column=(i - 1) % 3, sticky='nsew')
    else:
        button.grid(row=4, column=0, sticky='nsew')
    buttons.append(button)

####

# A selfmade switch statement for possible actions

def actionButton(text, act):
    global val
    global canAction
    global action
    numbertxt = int(text.get())
    if (canAction):
        if (action == Action.PLU):
            val += numbertxt
        elif (action == Action.MIN):
            val -= numbertxt
        elif (action == Action.TIM):
            val *= numbertxt
            val = int(val)
        elif (action == Action.DIV):
            if (numbertxt != 0):
                val /= numbertxt
                val = int(val)
            else:
                text.set('Impossible to divide by 0!')
        action = act
        if (action != Action.CLE):
            text.set(str(val))
        else:
            text.set('')
        if (action != Action.CLE):
                canAction = False
        else:
            action = Action.PLU

####

buttonplu = tk.Button(window, text='+', command=lambda: actionButton(text, Action.PLU))
buttonplu.grid(row=1, column=3, sticky='nsew')
buttonmin = tk.Button(window, text='-', command=lambda: actionButton(text, Action.MIN))
buttonmin.grid(row=2, column=3, sticky='nsew')
buttoncle = tk.Button(window, text='C', command=lambda: actionButton(text, Action.CLE))
buttoncle.grid(row=4, column=2, sticky='nsew')
buttontim = tk.Button(window, text='*', command=lambda: actionButton(text, Action.TIM))
buttontim.grid(row=3, column=3, sticky='nsew')
buttondiv = tk.Button(window, text='/', command=lambda: actionButton(text, Action.DIV))
buttondiv.grid(row=4, column=1, sticky='nsew')
buttonequ = tk.Button(window, text='=', command=lambda: actionButton(text, Action.EQU))
buttonequ.grid(row=4, column=3, sticky='nsew')

def num_key(event, num):
    numberButton(str(num), text)
for i in range(10):
    window.bind(str(i), lambda event, num=str(i): num_key(event, num))


def plus_key(event):
    buttonplu.invoke()
window.bind('+', plus_key)

def minus_key(event):
    buttonmin.invoke()
window.bind('-', minus_key)

def times_key(event):
    buttontim.invoke()
window.bind('*', times_key)

def div_key(event):
    buttondiv.invoke()
window.bind('/', div_key)

def clear_key(event):
    buttoncle.invoke()
window.bind('c', clear_key)

def equal_key(event):
    buttonequ.invoke()
window.bind('<Return>', equal_key)

tk.Grid.rowconfigure(window, 0, weight=1)
tk.Grid.rowconfigure(window, 1, weight=1)
tk.Grid.rowconfigure(window, 2, weight=1)
tk.Grid.rowconfigure(window, 3, weight=1)
tk.Grid.rowconfigure(window, 4, weight=1)
tk.Grid.columnconfigure(window, 0, weight=1)
tk.Grid.columnconfigure(window, 1, weight=1)
tk.Grid.columnconfigure(window, 2, weight=1)
tk.Grid.columnconfigure(window, 3, weight=1)


####

def resize(event):
    # Calculate the new font size based on the Entry widget's height
    new_size = -max(12, int(display.winfo_height() / 2))
    display['font'] = tkinter.font.Font(size=new_size)
    for button in buttons:
        button['font'] = tkinter.font.Font(size=new_size)
    buttonplu['font'] = tkinter.font.Font(size=new_size)
    buttonmin['font'] = tkinter.font.Font(size=new_size)
    buttoncle['font'] = tkinter.font.Font(size=new_size)
    buttontim['font'] = tkinter.font.Font(size=new_size)
    buttondiv['font'] = tkinter.font.Font(size=new_size)
    buttonequ['font'] = tkinter.font.Font(size=new_size)
window.bind('<Configure>', resize)


# Handling the closing and opening of the window
window.protocol('WM_DELETE_WINDOW', window.destroy)
window.mainloop()