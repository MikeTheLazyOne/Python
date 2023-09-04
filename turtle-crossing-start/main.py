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
score = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    
    cars.move()
    screen.update()
    # car colision logic
    for car in cars.list_of_cars:
        distance = car.distance(player)
        if distance <30:
            player.set_start_pos()
            score.game_over()
            
    # car finish logic
    xpos, ypos = player.pos()
    if ypos >= 300:
        score.update()
        player.set_start_pos()
        cars.level_up()

screen.exitonclick()