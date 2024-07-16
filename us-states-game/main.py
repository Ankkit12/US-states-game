import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

guessed_states = []
states = pandas.read_csv("50_states.csv")
state = states['state'].to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"States guessed {len(guessed_states)}/50", prompt="Enter the state name")
    answer_lower = answer_state.title()
    if answer_lower == "Exit":
        missing_states = [st for st in state if st not in guessed_states]
        # for st in state:
        #     if st not in guessed_states:
        #         missing_states.append(st)
        df = pandas.DataFrame(missing_states)
        df.to_csv('remaining_states.csv')
        break
    if answer_lower in state:
        guessed_states.append(answer_lower)
        row = states[states.state == f"{answer_lower}"]
        new = turtle.Turtle()
        new.hideturtle()
        new.penup()
        new.goto(int(row.iloc[0,1]), int(row.iloc[0,2]))
        new.write(f"{answer_lower}")
    




