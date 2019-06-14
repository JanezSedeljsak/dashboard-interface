import time
import tkinter
import pyfirmata
from pyfirmata import Arduino, util
from tkinter import *
##from python_RPi import branje

##Variables
##ledKitchen = 11

##def your arduino mount
board = Arduino('/dev/ttyACM0')

app = Tk()
app.title('Potato Interface')
app.geometry('450x300+200+200')

m = 11
pin_za = board.get_pin('d:11:p')

OPTIONS = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

##Set default value of drop down list
variable = StringVar(app)
variable.set(OPTIONS[13])

##State of light
State = 0


##Functions for light control
def TurnOnKitchen():
    board.digital[int(variable.get())].write(1)
    State = 1
    LKS1.configure(text=State)
    b1.configure(bg="green")
    b2.configure(bg="grey")
##    b3.configure(bg="grey")

def TurnOffKitchen():
    board.digital[int(variable.get())].write(0)
    State = 0
    LKS1.configure(text=State)
    b1.configure(bg="grey")
    b2.configure(bg="red")
##    b3.configure(bg="grey")

def KitchenSvetlostActivate():
    pin_za.write(Svetlost.get() / 10)
    State = Svetlost.get() / 10
    LKS1.configure(text=State)
    b1.configure(bg="grey")
    b2.configure(bg="grey")
##    b3.configure(bg="green")
    
def update():
    global m
    if m != int(variable.get()):
        b1.configure(bg="grey")
        b2.configure(bg="grey")
##        b3.configure(bg="grey")
    m = int(variable.get())
    
c = Label(app, text="Arduino PIN: ")
c.pack()
op1 = OptionMenu(app, variable, *OPTIONS)
op1.pack()
b1 = Button(app, text="ON", command=TurnOnKitchen, bg = "grey")
b1.pack(side=LEFT)
b2 = Button(app, text="OFF", command=TurnOffKitchen, bg = "grey")
b2.pack(side=LEFT)
c = Label(app, text="LED state: ")
c.pack()

LKS1 = Label(app, text=State)
LKS1.pack()

##PWM bar but for this all widgets need to have .pack()
##
Svetlost = Scale(app, from_=1, to=9, orient=HORIZONTAL)
Svetlost.pack( side = TOP )
b3 = Button(app, text="ON_BY_APPLY", command=KitchenSvetlostActivate, bg = "grey")
b3.pack( side = TOP )

b4 = Button(app, text="UPDATE", command=update, bg = "grey")
b4.pack()
##
##while True:
##    branje()
##    time.sleep(5)

app.mainloop()