from turtle import Screen, Turtle
import turtle
import pandas

screen = Screen()
screen.title("US State guessing game")

## Create background
image = "day-25_csv_data/state_guessing_game/blank_states_img.gif"
screen.addshape(image)
background = Turtle()
background.shape(image)

## Create scoreboard
scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,300)
scoreboard.write(f"Score: 0/50",move=False, align='center', font=('Arial', 20, 'normal'))


## Create state turtle
turtle.penup()
turtle.hideturtle()

## Import data
data = pandas.read_csv("day-25_csv_data/state_guessing_game/50_states.csv")


## Get coordinates  from click

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# answer_state = screen.textinput(title = "Guess a state:", prompt= "What is your guess?")
# answer_state = answer_state.title()

playing = True
guesses = []
score = 0
states = data.state.to_list()

while playing:
    answer_state = screen.textinput(title = "Guess a state (Type exit to exit)", prompt= "What is your guess?")
    answer_state = answer_state.title()
    if answer_state in states:
        states.remove(answer_state)
        guesses.append(guesses)
        turtle.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        turtle.write(str(answer_state), move=False, align='center', font=('Arial', 8, 'normal'))
        score += 1
        scoreboard.clear()
        scoreboard.write(f"Score: {score}/50",move=False, align='center', font=('Arial', 20, 'normal'))
    if answer_state == "Exit" or score == 50:
        playing = False


# Sates to learn
    states_to_learn = pandas.DataFrame(states)
    states_to_learn.to_csv("day-25_csv_data/state_guessing_game/states_to_learn.csv")
