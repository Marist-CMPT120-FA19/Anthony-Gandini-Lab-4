#Anthony Gandini

from graphics import *

def main():
    win = GraphWin("Traffic Light" , 1000 , 1000)
    body = Rectangle(Point(300 , 100) , Point(700 , 900))
    body.setFill("white")
    body.draw(win)
    
    redLight = Circle(Point(500 , 250) , 100)
    redLight.setFill("red")
    redLight.draw(win)
    
    yellowLight = Circle(Point(500 , 500) , 100)
    yellowLight.setFill("yellow")
    yellowLight.draw(win)
    
    greenLight = Circle(Point(500 , 750) , 100)
    greenLight.setFill("green")
    greenLight.draw(win)
    
main()