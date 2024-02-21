from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("/Downloads/data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"High score = {self.high_score} Score = {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Downloads/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", move=False, align='center', font=('Arial', 20, 'normal'))

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

        