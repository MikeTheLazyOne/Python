from turtle import Turtle

class Padle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.setposition(x = position, y = 0)
        self.shapesize(stretch_len = 1, stretch_wid = 5)
        self.pu()
        self.color("white")
    def up(self):
        xpos, ypos = self.pos()
        if ypos <= 350:
            self.goto(x = xpos, y = ypos + 20)
        else:
            print("Limit reached")
    def down(self):
        xpos, ypos = self.pos()
        if ypos >= -350:
            self.goto(x = xpos, y = ypos - 20)
        else:
            print("Limit reached")