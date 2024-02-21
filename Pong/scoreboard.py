from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_left} : {self.score_right}", move=False, align='center', font=('Arial', 20, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align='center', font=('Arial', 20, 'normal'))

    def score_increase(self, left_increase):
        if left_increase == True:
            self.score_left += 1
        elif left_increase != True: 
            self.score_right += 1
        self.clear()
        self.update_scoreboard()

        