from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=6)
        self.tilt(90)
        self.penup()
        self.speed(0)
        if player == "user":
            self.teleport(-785)
        else:
            self.teleport(778)

    def follow_mouse(self):
        x, y = screen.getcanvas().winfo_pointerx() - screen.window_width() // 2, screen.window_height() // 2 - screen.getcanvas().winfo_pointery()
        self.goto(x, y)
        screen.ontimer(fun=self.follow_mouse, t=10)
