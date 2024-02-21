from turtle import Turtle
snake_constant = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.sections = []
        self.create_snake()
        self.head = self.sections[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_section(position)

    def add_section(self, position):
        section = Turtle(shape = "square")
        section.color("white")
        section.penup()
        section.goto(position)
        self.sections.append(section)

    def reset(self):
        for section in self.sections:
            section.goto(1000,1000)
        self.sections.clear()
        self.create_snake()
        self.head = self.sections[0]
    
    def extend(self):
        self.add_section(self.sections[-1].position())

    def move(self):
        for section_num in range(len(self.sections)-1, 0, -1):
            new_x = self.sections[section_num - 1].xcor()
            new_y = self.sections[section_num - 1].ycor()
            self.sections[section_num].goto(new_x, new_y)
        self.head.forward(snake_constant)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            pass

