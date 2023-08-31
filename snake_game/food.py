from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self, shape : str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.new_position()

    def new_position(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x, y)