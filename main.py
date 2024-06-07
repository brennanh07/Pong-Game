from turtle import Screen
from pong_ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)


ball = Ball()

user_paddle = Paddle("user")
user_paddle.follow_mouse()
computer_paddle = Paddle("computer")


ball.get_starting_angle()

while True:
    ball.forward(5)



























screen.exitonclick()
