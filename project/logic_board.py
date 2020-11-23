#logic_board.py

from graphics import *
from tkinter import *
from graphic_gates import *



root = Tk()
root.title("logic board")
root.geometry("600x600")



def andGate():
    picA = draw_and(50,50,60,win)
    picA.pack()

def orGate():
    picB = draw_or(50,50,60,win)
    picB.pack()

def notGate():
    picC = draw_not(50,50,60,win)
    picC.pack()

def xorGate():
    picD = draw_xor(50,50,60,win)
    picD.pack()

def nandGate():
    picE = draw_nand(50,50,60,win)
    picE.pack()

    






    

btn1 = Button(root,text = "and gate",command=andGate)
btn1.pack()

btn2 = Button(root,text = "or gate",command=orGate)
btn2.pack()

btn3 = Button(root,text = "not gate",command=notGate)
btn3.pack()

btn4 = Button(root,text = "xor gate",command=xorGate)
btn4.pack()

btn5 = Button(root,text = "nand gate",command=nandGate)
btn5.pack()


    

root.mainloop()
    





    
