import turtle
import pandas

data = pandas.read_csv("50_states.csv")


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
for state in answer_state:
    if state in data:
        print("Hurray")
    else:
        print("Nay")


# Getting coordinates on the image of states.
# def get_mouse_clock_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_clock_coor)
# turtle.mainloop()
#
#
# # screen.exitonclick()