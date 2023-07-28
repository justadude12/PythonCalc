import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.eval('tk::PlaceWindow . center')
text = tk.StringVar()
text.set('')
display = tk.Entry(window, textvariable = text)
display.grid(row=0, column=0, columnspan=4)

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



button1 = tk.Button(window, text='1', command=lambda: numberButton('1', text))
button1.grid(row=1, column=0, sticky='nsew')
button2 = tk.Button(window, text='2', command=lambda: numberButton('2', text))
button2.grid(row=1, column=1, sticky='nsew')
button3 = tk.Button(window, text='3', command=lambda: numberButton('3', text))
button3.grid(row=1, column=2, sticky='nsew')
button4 = tk.Button(window, text='4', command=lambda: numberButton('4', text))
button4.grid(row=2, column=0, sticky='nsew')
button5 = tk.Button(window, text='5', command=lambda: numberButton('5', text))
button5.grid(row=2, column=1, sticky='nsew')
button6 = tk.Button(window, text='6', command=lambda: numberButton('6', text))
button6.grid(row=2, column=2, sticky='nsew')
button7 = tk.Button(window, text='7', command=lambda: numberButton('7', text))
button7.grid(row=3, column=0, sticky='nsew')
button8 = tk.Button(window, text='8', command=lambda: numberButton('8', text))
button8.grid(row=3, column=1, sticky='nsew')
button9 = tk.Button(window, text='9', command=lambda: numberButton('9', text))
button9.grid(row=3, column=2, sticky='nsew')
button0 = tk.Button(window, text='0', command=lambda: numberButton('0', text))
button0.grid(row=4, column=0, sticky='nsew')

####

# A selfmade switch statement for possible actions

def actionButton(text, act):
    global val
    global canAction
    global action
    numbertxt = int(text.get())
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
            text.set('Division par 0 impossible!')
    action = act
    if (action != Action.CLE):
        text.set(str(val))
    else:
        text.set('')
    if (action != Action.CLE):
        if(action != Action.EQU):
            canAction = False
        else:
            canAction = True
    else:
        action = Action.PLU

####

buttonplu = tk.Button(window, text='+', command=lambda: actionButton(text, Action.PLU))
buttonplu.grid(row=1, column=3)
buttonmin = tk.Button(window, text='-', command=lambda: actionButton(text, Action.MIN))
buttonmin.grid(row=2, column=3)
buttoncle = tk.Button(window, text='C', command=lambda: actionButton(text, Action.CLE))
buttoncle.grid(row=4, column=2)
buttontim = tk.Button(window, text='*', command=lambda: actionButton(text, Action.TIM))
buttontim.grid(row=3, column=3)
buttondiv = tk.Button(window, text='/', command=lambda: actionButton(text, Action.DIV))
buttondiv.grid(row=4, column=1)
buttonequ = tk.Button(window, text='=', command=lambda: actionButton(text, Action.EQU))
buttonequ.grid(row=4, column=3)

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

####

# Handling the closing and opening of the window
window.protocol('WM_DELETE_WINDOW', window.destroy)
window.mainloop()