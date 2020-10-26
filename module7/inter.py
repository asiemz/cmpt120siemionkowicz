from graphics import *
import math

def main():

    win=GraphWin("circle",300,300)
    win.setCoords(-10,-10,10,10)


    descr = Text(Point(0,0),"calculates intersection")
    click = Text(Point(0,-11), "click")
    descr.setSize(8)
    click.setSize(8)
    descr.draw(win)
    click.draw(win)

    win.getMouse()
    descr.undraw()
    


    radius = float(input("radius: "))
    intercept = float(input("y intercept: "))
    #rad_text.setSize(8)
    #int_text.setSize(8)
    #rad_text.draw(win)
    #int_text.draw(win)
    #rad_input = Entry(Point(0,5),3)
    #rad_input = Entry(Point(0,0),3)
    #rad_input.setSize(8)
    #int_input.setSize(8)
    #rad_input.draw(win)
    #int_input.draw(win)

    win.getMouse()
    #radius = eval(rad_input.getText())
    #intercept = eval(int_input.getText())
    #rad_text.undraw()
    #int_text.undraw()
    #rad_input.undraw()
    #int_input.undraw()
    #click.undraw()

    xint1 = -math.sqrt(radius**2 - intercept**2)
    xint2 = math.sqrt(radius**2 - intercept**2)

    x_axis = Line(Point(-10,0), Point(10,0))
    x_axis.setArrow("last")
    y_axis = Line(Point(0,-10),Point(0,10))
    y_axis.setArrow("last")
    circ = Circle(Point(0,-10),radius)
    circ.setOutline("blue")
    line = Line(Point(-10,intercept),Point(10,intercept))
    line.setOutline("blue")
    int1= Circle(Point(xint1, intercept),0.2)
    int1 = setFill("red")
    int1.setOutline("red")
    int2 = Circle(Point(xint2, intercept), 0.2)
    int2.setFill("red")
    int2.setOutline("red")
    x_axis.draw(win)
    y_axis.draw(win)
    circ.draw(win)
    line.draw(win)
    int1.draw(win)
    int2.draw(win)

    int_info = Text(Point(0,-11), "x values of points of/n" + "intersection: " + str(xint1) + "," +  str(xint2))

    int_info.setSize(8)
    int_info.draw(win)

    win.getMouse()
    win.close()

main()
