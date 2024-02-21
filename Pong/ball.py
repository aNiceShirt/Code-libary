from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len= 1, stretch_wid= 1)
        self.goto(0,0)

    def move(self,direction_x, direction_y):
        new_y = self.ycor() + 1 * direction_y
        new_x = self.xcor() + 1 * direction_x
        self.goto(new_x,new_y)
        
    def refresh(self):
        self.goto(0,0)
        

