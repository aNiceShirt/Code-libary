from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
        
    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setheading(0)
        self.goto(position,0)
    
    def up(self):
        new_y = self.ycor() + 30
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.sety(new_y)

