import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        '''
        missing_states = [new_item for item in list if test]
        '''
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state in all_states:
        #         missing_states.append(state)
        # # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)







# Getting coordinates on the image of states.
# def get_mouse_clock_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_clock_coor)
# turtle.mainloop()
#
#
# screen.exitonclick()
