from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=6)
        self.tilt(90)
        self.penup()
        self.speed(0)
        if player == "user":
            self.teleport(-785)
            self.locked_x = -785
        else:
            self.teleport(778)
        self.color("white")

    def follow_mouse(self):
        y = screen.window_height() // 2 - screen.getcanvas().winfo_pointery()
        self.goto(self.locked_x, y)
        screen.ontimer(fun=self.follow_mouse, t=10)

    def move(self):
        if self.ycor() < 475:
            self.setheading(90)
            self.forward(1)
        else:
            self.setheading(270)
            self.back(1)




