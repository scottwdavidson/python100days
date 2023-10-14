from turtle import Turtle

class Etchy:

    etchy = Turtle()

    def __int__(self):
        self.etchy.shape("arrow")
        self.etchy.pensize(5)
        self.etchy.pencolor("white")

    def move_forwards(self):
        self.etchy.forward(10)


    def move_backwards(self):
        self.etchy.backward(10)


    def move_right(self):
        self.etchy.right(10)
        self.move_forwards()


    def move_left(self):
        self.etchy.left(10)
        self.move_forwards()

    def clear(self):
        self.etchy.clear()
        self.etchy.penup()
        self.etchy.home()
        self.etchy.pendown()
