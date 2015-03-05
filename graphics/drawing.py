
from graphics import *
import random

win = GraphWin("window", 500, 500)

file = open("data.txt")
data = file.readlines()

l = 20
i = 1

for line in data:
    randColR = random.randint(100,254)
    randColG = random.randint(100,254)
    randColB = random.randint(100,254)
    randPointX = random.randint(0,499)
    randPointY = random.randint(0,499)
    randNum = random.randint(0,31)
    
    c = Circle(Point(randPointX,randPointY),float(data[randNum]))
    c.setFill(color_rgb(randColR,randColG,randColB))
    c.setWidth(0)
    c.draw(win)
    
    t = Text(Point(randPointX,randPointY), data[randNum])
    t.setText('Radius = ' + data[randNum])
    t.setSize(10)
    t.draw(win)

#c = Circle(Point(250,250), float(data[28]))
#c.draw(win)

win.getMouse() # pause for click in window
win.close()
    
