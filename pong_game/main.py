from turtle import Turtle, Screen
from padle import Padle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.colormode(255)
screen.title("Pong")
screen.tracer(0)


R_Paddle = Padle(350)
L_Paddle = Padle(-350)

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun= R_Paddle.up)
screen.onkey(key="Down", fun = R_Paddle.down)
screen.onkey(key="w", fun=L_Paddle.up)
screen.onkey(key="s", fun=L_Paddle.down)

game_status = True


while(game_status == True):
    screen.update()
    time.sleep(0.01)
    ball.move()

    xball, yball = ball.pos()


    # Border logic
    if yball >= 300 or yball <= -300: 
        ball.bouce()
    elif xball >= 400 or xball <= -400:
        if xball >=400:
            score.l_point()
        if xball <= -400:
            score.r_point()
        ball.start_over()
    
    
    # Padle logic collision
    if 360 > ball.xpos >340 and R_Paddle.distance(ball) < 50:
        ball.hit()
    elif -360 < ball.xpos < -340 and L_Paddle.distance(ball) < 50:
        ball.hit()
    

screen.exitonclick()