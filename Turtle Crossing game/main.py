import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Game")
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 270:
        player.starting()
        car_manager.faster_cars()
        scoreboard.score_increase()

    screen.update()

screen.exitonclick()




## TODO
# Delete car when reaching end of screen
# Manage where car can spawn so no two cars spawn on each other
