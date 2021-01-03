from turtle import Turtle


class Vehicle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.goto(0, -340)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def go_to_start(self):
        self.goto(0, -340)

