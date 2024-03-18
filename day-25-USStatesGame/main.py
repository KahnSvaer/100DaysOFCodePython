from turtle import Screen, Turtle
import pandas
import pandas as pd

FONT = ("arial", 8, "normal")

# writer setup
writer_turtle = Turtle()
writer_turtle.penup()
writer_turtle.ht()
writer_turtle.speed("fastest")


# writer function
def write(state_name, x, y):
    """
    Writes the name of the state on the screen
    :param str state_name:
    :param float x:
    :param float y:
    :return: none
    """
    writer_turtle.goto(x, y)
    writer_turtle.write(f"{state_name}", align="center", font=FONT)


states_df = pandas.read_csv("50_states.csv")
not_found_states_list = states_df.state.to_list()
total_states = len(not_found_states_list)

# Screen Setup
screen = Screen()
screen.setup(725, 491)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
image_turtle = Turtle()
image_turtle.shape(image)

while len(not_found_states_list):
    new_state = screen.textinput(title=f"{total_states - len(not_found_states_list)}/{total_states} guessed correctly",
                                 prompt="Enter another state name: ").title()
    if new_state == "Exit":
        break
    if new_state in not_found_states_list:
        not_found_states_list.remove(new_state)
        df_row = states_df[states_df["state"] == new_state]
        new_x = df_row.x.item()
        new_y = df_row.y.item()
        write(new_state, new_x, new_y)

to_learn_dic = {"state": not_found_states_list}
pd.DataFrame(to_learn_dic).to_csv("states_to_learn.csv")
