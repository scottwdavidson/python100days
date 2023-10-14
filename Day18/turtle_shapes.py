import random
from turtle import Turtle, Screen

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def random_color_255():
    return random.randint(0, 0xFF)

def draw_closed_shape(turtle, sides, side_length):
    angle = 360/sides

    print(f"angle = {angle} , " + str(sides*angle))

    for _ in range(sides):
        r = random_color_255()
        g = random_color_255()
        b = random_color_255()
        turtle.pencolor(r,g,b)
        turtle.forward(side_length)
        turtle.right(angle)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    LENGTH = 75

    screen = Screen()
    screen.colormode(255)
    tim = Turtle()
    tim.penup()
    tim.left(90)
    tim.forward(200)
    tim.left(90)
    tim.forward(LENGTH)
    tim.right(180)
    tim.pendown()
    for number_of_sides in range(3,19):
        tim.shape(random.choice(screen.getshapes()))
        draw_closed_shape(tim,int(number_of_sides),LENGTH)


    screen.exitonclick()