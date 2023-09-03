from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSIBLE_POSITION = list(range(-275,276,5))
POSIBLE_POSITION_RIGHT = list(range(280,320,5))
POSIBLE_POSITION_LEFT = list(range(-320,-280,5))

class CarManager():
    
    def __init__(self) -> None:

        self.number_of_cars = 10
        self.list_of_cars = list()
        self.set_up()

    def new_turtle(self):
        # print("Car was created")
        turtle = Turtle(shape="square")
        turtle.shapesize(stretch_wid=1,stretch_len=2)
        turtle.color(random.choice(COLORS))
        turtle.pu()
        heading = [1, 2]
        if random.choice(heading) == 1:
            turtle.seth(180)
            turtle.setpos(random.choice(POSIBLE_POSITION_RIGHT),random.choice(POSIBLE_POSITION))
        else:
            turtle.setheading(0)
            turtle.setpos(random.choice(POSIBLE_POSITION_LEFT),random.choice(POSIBLE_POSITION))
        self.list_of_cars.append(turtle)
        # print(self.list_of_cars)
    def move(self):
        i = 0
        while i < len(self.list_of_cars):
            turtles = self.list_of_cars[i]
            turtles.fd(10)
            xpos, ypos = turtles.pos()
            if xpos >= 330 or xpos <= -330:
                turtles.clear()
                turtles.hideturtle()
                self.list_of_cars.remove(turtles)
                # print("car was removed")
                self.new_turtle()
            else:
                i += 1

            
    def set_up(self):
        for i in range(self.number_of_cars):
            
            self.new_turtle()
    
    def colision(self, turtle):
        for cars in self.list_of_cars:
            distance = cars.distance(turtle)
            if distance < 30:
                return True
            else:
                return False
