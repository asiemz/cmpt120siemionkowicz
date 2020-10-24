
from graphics import *

def main():

    win = GraphWin("bullseye",400,400)
    center = Point(200,200)

    white = Circle(center,150)
    white.setFill("white")
    white.draw(win)

    black = Circle(center,120)
    black.setFill("black")
    black.draw(win)

    blue = Circle(center,90)
    blue.setFill("blue")
    blue.draw(win)

    red = Circle(center, 60)
    red.setFill("red")
    red.draw(win)

    yellow = Circle(center, 30)
    yellow.setFill("yellow")
    yellow.draw(win)

    win.getMouse()
    win.close()

main()

    
