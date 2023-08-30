from turtle import Turtle, Screen
import time
from snake import Snake



screen = Screen()
screen.bgcolor("black")
screen.setup(width= 600, height=600)
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.Up_Heading)
screen.onkey(key="Down", fun=snake.Down_Heading)
screen.onkey(key="Left", fun=snake.Left_Heading)
screen.onkey(key="Right", fun=snake.Right_Heading)

game_status = True

while(game_status == True):
    snake.move()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()