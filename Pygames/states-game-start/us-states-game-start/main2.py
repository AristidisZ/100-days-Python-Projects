import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(700, 600)
screen.title("U.S States Game")
image_path = "blank_states_img.gif"
turtle.addshape(image_path)
turtle.shape(image_path)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/{len(all_states)} States Correct",
                                    prompt="give a guess").title()

    if answer_state == "Exit".title():
        missed_states = []
        for i in all_states:
            if i not in guessed_state:
                missed_states.append(i)
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("states_to_learns.csv")
        break

    if answer_state in all_states and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.mainloop()
