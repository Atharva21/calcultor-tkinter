from tkinter import *
my_font = ("Consolas 12 bold")
BUTTON_HT = 3
BUTTON_WIDTH = 6

root = Tk()
root.geometry("+500+200")
root.title("Calculator")
root.resizable(False, False)   ##make window size fixed.

equation = StringVar()      #make label a string var as its value changes constantly.
equa = ""
equation.set("Enter Expression.")

def btnPressed(num):
    global equa
    equa += str(num)
    equation.set(equa)

def equalsPressed():
    global equa
    try:
        total = eval(equa)
    except Exception as w:
        print(str(w))
        return
    equa = str(total)
    equation.set(equa)

def delPressed():
    global equa
    temp = []
    for i in equa:
        temp.append(i)
    try:
        temp.pop()
    except Exception as w:
        print(str(w))
        return
    equa = ""
    for i in temp:
        equa += str(i)
    equation.set(equa)

def clrEq():
    global equa
    equa = ""
    equation.set(equa)

ansLabel = Label(root, textvariable = equation, font = ("Consolas", 16), height = BUTTON_HT)
ansLabel.grid(columnspan = 5, sticky = NSEW)

########BUTTONS#############

button0 = Button(root, text = "0", command = lambda:btnPressed(0), height = BUTTON_HT, width = BUTTON_WIDTH)
button0.grid(row = 4, column = 1)

button1 = Button(root, text = "1", command = lambda:btnPressed(1), height = BUTTON_HT, width = BUTTON_WIDTH)
button1.grid(row = 3, column = 0)

button2 = Button(root, text = "2", command = lambda:btnPressed(2), height = BUTTON_HT, width = BUTTON_WIDTH)
button2.grid(row = 3, column = 1)

button3 = Button(root, text = "3", command = lambda:btnPressed(3), height = BUTTON_HT, width = BUTTON_WIDTH)
button3.grid(row = 3, column = 2)

button4 = Button(root, text = "4", command = lambda:btnPressed(4), height = BUTTON_HT, width = BUTTON_WIDTH)
button4.grid(row = 2, column = 0)

button5 = Button(root, text = "5", command = lambda:btnPressed(5), height = BUTTON_HT, width = BUTTON_WIDTH)
button5.grid(row = 2, column = 1)

button6 = Button(root, text = "6", command = lambda:btnPressed(6), height = BUTTON_HT, width = BUTTON_WIDTH)
button6.grid(row = 2, column = 2)

button7 = Button(root, text = "7", command = lambda:btnPressed(7), height = BUTTON_HT, width = BUTTON_WIDTH)
button7.grid(row = 1, column = 0)

button8 = Button(root, text = "8", command = lambda:btnPressed(8), height = BUTTON_HT, width = BUTTON_WIDTH)
button8.grid(row = 1, column = 1)

button9 = Button(root, text = "9", command = lambda:btnPressed(9), height = BUTTON_HT, width = BUTTON_WIDTH)
button9.grid(row = 1, column = 2)

plus = Button(root, text = "+", command = lambda:btnPressed('+'), height = BUTTON_HT, width = BUTTON_WIDTH)
plus.grid(row = 4, column = 3)

minus = Button(root, text = "-", command = lambda:btnPressed('-'), height = BUTTON_HT, width = BUTTON_WIDTH)
minus.grid(row = 3, column = 3)

divide = Button(root, text = "/", command = lambda:btnPressed('/'), height = BUTTON_HT, width = BUTTON_WIDTH)
divide.grid(row = 2, column = 3)

multiply = Button(root, text = "*", command = lambda:btnPressed('*'), height = BUTTON_HT, width = BUTTON_WIDTH)
multiply.grid(row = 1, column = 3)

clear = Button(root, text = "C", command = clrEq, height = BUTTON_HT, width = BUTTON_WIDTH)
clear.grid(row = 4, column = 0)

equals = Button(root, text = "=", command = equalsPressed, height = (2 * BUTTON_HT) + 1, width = BUTTON_WIDTH)
equals.grid(row = 3, column = 4, rowspan = 2)

dotButton = Button(root, text = ".", command = lambda:btnPressed('.'), height = BUTTON_HT, width = BUTTON_WIDTH)
dotButton.grid(row = 1, column = 4)

mod = Button(root, text = "%", command = lambda:btnPressed('%'), height = BUTTON_HT, width = BUTTON_WIDTH)
mod.grid(row = 2, column = 4)

Delete = Button(root, text = "Del", command = delPressed, height = BUTTON_HT, width = BUTTON_WIDTH)
Delete.grid(row = 4, column = 2)

#LOOP#
root.mainloop()
