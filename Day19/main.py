# This is a sample Python script.
from turtle import Turtle, Screen
import random


def create_turtle(color, relative_position):
    new_turtle = Turtle()
    new_turtle.color(color)
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.setposition(x=-225, y=(-125 + relative_position * 50))
    return new_turtle


def random_distance():
    return random.randint(5, 17)


def move_turtle(active_turtle, distance):
    active_turtle.forward(distance)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # setup the screen and get user bet
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 400
    TURTLE_COLORS = ["purple", "blue", "green", "yellow", "orange", "red"]
    FINISH_LINE_X_COR = 215
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    turtles = []
    for index in range(len(TURTLE_COLORS)):
        turtles.append(create_turtle(TURTLE_COLORS[index], index))

    user_bet = screen.textinput("Welcome to the Turtle Races", "Pick the winning turtle by color: ").lower()
    print(f"{user_bet}")

    still_racing = True
    winning_turtle = None
    while still_racing:

        for index in range(len(TURTLE_COLORS)):

            # move the turtle forward
            move_turtle(turtles[index], random_distance())

            # check to see if turtle won
            if turtles[index].xcor() >= FINISH_LINE_X_COR:
                print(f"{turtles[index].fillcolor()} : WON !!! ( {turtles[index].xcor()} )")
                still_racing = False
                winning_turtle = turtles[index]
                break


    # winner or loser ?
    if user_bet == winning_turtle.fillcolor():
        print(f"You picked {user_bet} and it's a WINNER !!")
    else:
        print(f"You picked {user_bet} and it's a LOSER !!")


    screen.exitonclick()
