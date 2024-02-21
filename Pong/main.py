# Import required modules
from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen_width = 800
screen_height = 600
# Set up the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)

left_paddle = Paddle(-screen_width/2 + screen_width/20)
right_paddle = Paddle(screen_width/2 - screen_width/20)
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(left_paddle.up, "w") 
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True
direction_y = 1
direction_x = 1
game_speed = 0.008

while game_is_on:
    screen.update()

    ## Top or bottom wall detection
    if ball.ycor() > (screen_height-30)/2:
        direction_y = -1

    elif ball.ycor() < -(screen_height-30)/2:
        direction_y = 1

    if ball.distance(left_paddle) < 50 and ball.xcor() < -screen_width/2 + screen_width/20 + 20:
        direction_x = 1
        game_speed *=0.9

    elif ball.distance(right_paddle) < 50 and ball.xcor() > screen_width/2 - screen_width/20 - 20:
        direction_x = -1
        game_speed *=0.9

    ## Right or left wall detection
    # Left wins
    if ball.xcor() > (screen_width-40)/2:
        scoreboard.score_increase(True)
        ball.refresh()
        game_speed = 0.008
        direction_x *= -1
    # Right wins
    elif ball.xcor() < -(screen_width-40)/2:
        scoreboard.score_increase(False)
        ball.refresh()
        game_speed = 0.008
        direction_x *= -1
    
    ball.move(direction_x=direction_x, direction_y=direction_y)
    time.sleep(game_speed)

screen.exitonclick()