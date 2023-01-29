import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
answer_list = []

while len(answer_list) < 50:
    answer_state = screen.textinput(title=f"{len(answer_list)}/50 Sates Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_to_learn = []
        for state in states_list:
            if state not in answer_list:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(arg=answer_state, align="center", font=("Arial", 10, "normal"))
        answer_list.append(answer_state)
