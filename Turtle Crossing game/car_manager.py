from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LANES = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.MOVE_INCREMENT = MOVE_INCREMENT
        
    def create_car(self): 
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle(shape = "square")
            car.color(COLORS[random.randint(0,len(COLORS)-1)])
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(280,random.randint(-24,26)*10)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.MOVE_INCREMENT)

    def faster_cars(self):
        self.MOVE_INCREMENT *= 1.1

    def delete_car (self, car):
        self.cars.remove(car)




    
