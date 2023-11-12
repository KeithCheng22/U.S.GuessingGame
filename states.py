from turtle import Turtle



class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def write_state(self, coord, answer_state):
        self.hideturtle()
        self.penup()
        self.goto(coord)
        self.pendown()
        self.color("black")
        self.write(answer_state, align="center")
