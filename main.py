import pandas
import turtle

FONT = ('Arial', 10, 'normal')
ALIGNMENT = "center"

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def write_state(x, y):
    map_text = turtle.Turtle()
    map_text.hideturtle()
    map_text.color("black")
    map_text.penup()
    map_text.goto(x, y)
    map_text.write(answer_state, False, font=FONT, align=ALIGNMENT)
    on_screen_text.append(map_text)


data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()

#Gameplay loop
correct_answers = []

on_screen_text = []
while len(correct_answers) < 50:
    if len(correct_answers) > 0:
        answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Guessed", prompt="Can you name another US "
                                                                                            "State?").title()
    else:
        answer_state = screen.textinput(title=f"Guess The States", prompt="Can you name a US State?").title()

    if answer_state in correct_answers:
        pass
    elif answer_state == "Exit":
        missing_answers = [state for state in all_states if state not in correct_answers]
        new_data = pandas.DataFrame(missing_answers)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in all_states:
        correct_answers.append(answer_state)
        data_row = data[data.state == answer_state]
        x = int(data_row.x)
        y = int(data_row.y)
        write_state(x, y)



