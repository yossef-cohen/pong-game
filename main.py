import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


count = True
game_is_on = True
while game_is_on:
    time.sleep(ball.speed_up)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and count:
        ball.bounce_x()
        count = False

    if ball.distance(l_paddle) < 50 and not count:
        ball.bounce_x()
        count = True

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        count = False

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        count = True

screen.exitonclick()
