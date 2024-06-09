from turtle import Screen
from pong_ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.tracer(0)


ball = Ball()

user_paddle = Paddle("user")
user_paddle.follow_mouse()
computer_paddle = Paddle("computer")

score = 0

play_game = True

while play_game:
    screen.update()
    ball.move()
    if ball.ycor() >= 478 or ball.ycor() <= -470:
        ball.bounce("y")
    elif ball.distance(user_paddle) < 40 and ball.xcor() < -780:
        ball.bounce("x")
    elif ball.distance(computer_paddle) < 40 and ball.xcor() > 780:
        ball.bounce("x")

    if ball.xcor() < -815:
        ball = Ball()
        ball.move()
    elif ball.xcor() > 815:
        ball = Ball()
        ball.move()
        score += 1




























screen.exitonclick()
