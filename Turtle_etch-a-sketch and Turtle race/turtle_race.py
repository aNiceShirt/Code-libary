from turtle import Turtle, Screen
import random

turtle_colors = ["red", "orange", "blue", "purple", "green", "yellow", "black", "gray"]
all_turtles = []
is_race_on = False

screen = Screen()
height = 400
width = 500
screen.setup(width=width, height=height)
user_bet = screen.textinput(title="Turtle race - Place your bet", prompt=f"What color of turtle will win the race?: {turtle_colors}").lower()


while user_bet not in turtle_colors:
    user_bet = screen.textinput(title="Please select from the availible colors", prompt=f"What color of turtle will win the race?: {turtle_colors}").lower()

random.shuffle(turtle_colors)

i = 0
y_coordinate = height/2 *-1 + height/len(turtle_colors)/2
for new_turtle in turtle_colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[i])
    new_turtle.goto(x=width/-2 +20, y=y_coordinate)
    i += 1
    y_coordinate += height/len(turtle_colors)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= width/2 -30:
            winning_turtle = turtle.color()[0]
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


print(f"{winning_turtle.capitalize()} turtle has won!")
if user_bet == winning_turtle:
    print("You won the bet, congratulations!")
else:
    print(f"You chose the {user_bet} turtle. So you lost the bet, sorry.")


screen.exitonclick()