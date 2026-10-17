#import osztaly
#t1= osztaly.Teglalap() 
#print(t1.kerulet()
#Autoverseny 

import turtle
class Auto(turtle.Turtle):
    def __init__(self, szin, x, y, sebesseg):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.goto(x, y)
        self.sebesseg = sebesseg

    def indit (self):
        self.forward(self.sebesseg)



ablak = turtle.Screen()
ablak.bgcolor("white")
ablak.title("Autoverseny")
a1 = Auto("red", -200, 0, 5)
a2 = Auto("blue", -200, -50, 5)
ablak.listen()

ablak.onkey(turtle.bye, key="Escape")
ablak.onkey(a1.indit, key="d")
ablak.onkey(a2.indit, key="k")
turtle.mainloop()
