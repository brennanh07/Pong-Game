from turtle import Turtle
import random


starting_angles = [[x for x in range(-31, 32)], [y for y in range(149, 211)]]






class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1.6)
        self.penup()

    def get_starting_angle(self):
        random_angle = random.choice(random.choice(starting_angles))
        self.setheading(random_angle)
        # self.forward(5)
