from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0 
        self.r_score = 0
        self.pu()
        self.borders()
        self.update()

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()

    def update(self):
        self.clear()
        self.borders()
        self.setpos(-180, 280)
        self.write(arg=self.l_score, align="center", font=("courier", 80, "normal"))
        self.setpos(180, 280)
        self.write(arg=self.r_score, align="center", font=("courier", 80, "normal"))
    
    def borders(self):
        self.pencolor("white")
        self.width(5)
        self.setpos(-400,300)
        self.pd()
        self.goto(400,300)
        self.goto(400,-300)
        self.goto(-400,-300)
        self.goto(-400,300)
        self.pu()