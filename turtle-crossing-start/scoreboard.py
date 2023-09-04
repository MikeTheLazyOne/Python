from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.pu()
        self.setpos(-280, 280)
        self.score = 0 
        self.write(arg=f"Score: {self.score}",align="left", font=FONT)
        self.hideturtle()
        
    def update(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}",align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(arg=f"GAME OVER\nyour score is {self.score}",align="left", font=FONT)
