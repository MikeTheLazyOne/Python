from turtle import Turtle
import random



class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.pu()
        self.color("white")
        self.setheading(random.randint(0, 360))
        self.speed = 2
    def move(self):
        self.xpos, self.ypos = self.pos()
        self.fd(self.speed)
        if 80 <=self.heading() <= 100 or 260 <= self.heading() <= 280:
            self.seth(random.randint(0, 360))
        
    def bouce(self):
        self.seth(360 - self.heading())
    
    def start_over(self):
        self.speed = 2
        self.setpos(0,0)
        self.seth(random.randint(0,360))
    def hit(self):
        self.seth(180 - self.heading())
        self.fd(self.speed + 10)
        self.speed += 1