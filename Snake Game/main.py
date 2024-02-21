from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

## Screen settings ##
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorebaord = Scoreboard()

## Keybindings ##
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


## Game ##
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Eat food
    if snake.head.distance(food.pos()) < 15:
        food.refresh()
        scorebaord.score_increase()
        snake.extend()
        
    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor()< -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scorebaord.reset()
        snake.reset()

    # Detect collision with tail
    for section in snake.sections[1:]:
        if snake.head.distance(section) < 10:
            scorebaord.reset()
            snake.reset()



screen.exitonclick()