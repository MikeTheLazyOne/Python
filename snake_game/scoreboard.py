from turtle import Turtle
import random
ALIGMENT = "center"
FONT = ("Ariel", 12, "normal")

class ScoreBoard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.read_data()
        self.high_score = int(self.data_socre)
        self.goto(x=0, y= 280)
        self.color("white")
        self.write(arg=f"Score: {self.score}, Highscore: {self.data_socre}", align = ALIGMENT, font = FONT) 

    def plus_one(self):
        
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game over, Score: {self.score}", align = ALIGMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.read_data()
            if int(self.data_socre) < self.high_score:
                self.write_data()
        
        self.score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score = {self.high_score}", align = ALIGMENT, font = FONT)
    def read_data(self):
        with open("data.txt","r")as file:
            self.data_socre = file.read()
    def write_data(self):
        with open("data.txt","w")as file:
            file.write(f"{self.score}")
