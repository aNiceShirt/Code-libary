###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('J:/Google Drive/Coding/Python/100Days of Code Python/Code libary/Turtle/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
    
# print(rgb_colors)

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("chartreuse4")
my_screen = Screen()
my_screen.colormode(255)
timmy.speed(0)
timmy.hideturtle()   


color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
def draw_dot_pattern(grid_size, dot_size,spacing):
    for i in range(grid_size):
        timmy.penup()
        timmy.sety(i*grid_size*spacing)
        timmy.setx(0)
        for j in range(grid_size):
            timmy.penup()
            timmy.forward(grid_size*spacing)
            timmy.dot(dot_size, random.choice(color_list))


draw_dot_pattern(5,20,5)
my_screen.exitonclick()