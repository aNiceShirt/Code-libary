from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

sensitivity = 20

def move_forward():
    tim.forward(sensitivity)

def move_backward():
    tim.backward(sensitivity)

def reset_screen():
    tim.home()
    tim.clear()

def turn_right():
    tim.right(sensitivity/2)

def turn_left():
    tim.left(sensitivity/2)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_screen)



screen.exitonclick()