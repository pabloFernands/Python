import turtle
import pandas

screen = turtle.Screen()
screen.title("Map of USA")
image_background = "mapa_brasil.gif"
#screen.bgpic(image_background)
screen.addshape(image_background)
turtle.shape(image_background)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
guess = 0
data = pandas.read_csv("27_states.csv")
all_states = data.state.to_list()
guessed_states = []

for x in range(26):

    answer_state = screen.textinput(title=f"Guess? {guess} States Correct", prompt="What's another "
                                                                                   "state's name?").title()
    print(answer_state)

    if answer_state in all_states:
        guessed_states.append(answer_state)
        guess += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        print("acertou")

    elif answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

states_guess_correct = list(set(all_states) - set(guessed_states))

data_dict = {
    "States Missing": [states_guess_correct],
    "Count of Missing States": [len(states_guess_correct)]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("states_to_learn.csv")

turtle.mainloop()

# screen.exitonclick()