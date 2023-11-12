import turtle
import pandas
from states import State

state_name = State()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
correct_guess = []
data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()
while len(correct_guess) < 50:
    coord = []
    answer_state = screen.textinput(title=f"Score: {score}/50", prompt="What's another state name?").title()

    if answer_state == "Exit":
        break
    for state in state_names:
        if state == answer_state:
            state = data[data.state == answer_state]
            state_coord_x = int(state["x"])
            state_coord_y = int(state["y"])
            coord.append(state_coord_x)
            coord.append(state_coord_y)
            state_name.write_state(coord, answer_state)

            if answer_state not in correct_guess:
                correct_guess.append(answer_state)
                score += 1

to_learn = [state for state in state_names if state not in correct_guess]
data = pandas.DataFrame(to_learn)
data.to_csv("states_to_learn.csv")

screen.exitonclick()
