from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 600, height=600)
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

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

    # dectectig colisions with food
    if snake.head.distance(food) < 20:
        print("nom nom nom")
        food.new_position()
        score.plus_one()
        snake.new_body()
    
    # Detecting wall colisions
    if snake.head.xcor() > 290 or\
       snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        print("you hit the wall")
        print("game over")

        score.reset()
        snake.reset()
        # score.game_over()
        # game_status = False 

    # # Dectecting colisions with tail
    # for seg in snake.snake_list:
    #     if snake.head.distance(seg) < 5:
    #         if snake.head != seg:
    #             score.game_over()
    #             game_status = False
    #             print("you ate your tail")
     # Dectecting colisions with tail
    for seg in snake.snake_list[1:]:
        if snake.head.distance(seg) < 5:
            
            score.reset()
            snake.reset()
            # score.game_over()
            # game_status = False
            print("you ate your tail")


screen.exitonclick()