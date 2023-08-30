from turtle import Turtle

MOVECONSTAT = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        
        self.snake_list = list()
        
        self.start_body(3)

    def new_body(self):
        new_body = Turtle()
        new_body.pu()
        new_body.color("white")
        new_body.shape("square")
        self.snake_list.append(new_body)

    def start_body(self, size):
        for i in range(size):
            print(i)
            self.new_body()
            self.snake_list[i].setx(-20*i)
        self.head = self.snake_list[0]
    def move(self):
        for i in range(len(self.snake_list)-1,0, -1):
        
            seg_prev = self.snake_list[i-1]
            seg =self.snake_list[i]
            prev_pos = seg_prev.pos()
            print(prev_pos)
            seg.setpos(prev_pos)
        self.snake_list[0].fd(MOVECONSTAT)
    def Up_Heading(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        else:
            print("Can't make this move")

    def Down_Heading(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        else:
            print("Can't make this move")

    def Left_Heading(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        else:
            print("Can't make this move")
    def Right_Heading(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        else:
            print("Can't make this move")


    
    