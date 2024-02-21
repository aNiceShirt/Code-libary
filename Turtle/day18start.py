from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("chartreuse4")
my_screen = Screen()
my_screen.colormode(255)

## Box
# for i in range(0,4):
#     timmy.forward(100)
#     timmy.right(90)

# ## Dashed line
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# ## Multiple shapes diff colors
# for i in range(3,11):
#     timmy.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
#     for j in range(i):
#         timmy.forward(100)
#         timmy.right(360/i)

# ## Random direction random colors
# def random_color():
#     color = random.randint(0,255), random.randint(0,255), random.randint(0,255)
#     return color


# def random_direction(num_directions):
#     turn_amount = 360 / num_directions
#     direction = turn_amount*random.randint(0,num_directions-1)
#     print(direction)
#     return direction

# timmy.speed(0)
# timmy.pensize(10)

# for i in range (300):
#     timmy.pencolor(random_color())
#     timmy.setheading(random_direction(21))
#     timmy.forward(30)

## Draw spiral
# timmy.speed(0)
# timmy.pensize(2)

# def random_color():
#     color = random.randint(0,255), random.randint(0,255), random.randint(0,255)
#     return color

# def draw_spiral(gap):
#     for i in range(0,360+1,int(gap)):
#         timmy.pencolor(random_color())
#         timmy.circle(100)
#         timmy.setheading(i)

# draw_spiral(4)


my_screen.exitonclick()
