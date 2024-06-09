from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1.6)
        self.penup()
        self.x_move = 0.3
        self.y_move = 0.3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, side):
        if side == "x":
            self.x_move *= -1
        else:
            self.y_move *= -1
