import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    
    cars.move()
    screen.update()
    # car colision logic
    if cars.colision(player) == True:
        print("GAME OVER")
    

    # car finish logic
screen.exitonclick()