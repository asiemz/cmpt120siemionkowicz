#line.py

from graphics import *
from math import sqrt


def main():

    win = GraphWin("line",300,300)

    text = Text(Point(150,20), "2 mouse clicks")
    text.setSize(8)
    text.draw(win)

    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    line = Line(point1,point2)
    line.setWidth(2)
    line.draw(win)

    midpointx = (point1.getX() + point2.getX()) / 2
    midpointy = (point1.getY() + point2.getY()) / 2
    midpoint = Circle(Point(midpointx, midpointy), 2)
    midpoint.setOutline("red")
    midpoint.setFill("red")
    midpoint.draw(win)

    disx = point2.getX() - point1.getX()
    disy = point2.getY() - point1.getY()
    slope = - disy/disx

    length = sqrt(disx**2 + disy**2)
    text.setText("slope: " + format(slope, "0.4") + "\nLength: " + \
                 format(length, "0.4") + "px")

    win.getMouse()
    win.close()

main()
