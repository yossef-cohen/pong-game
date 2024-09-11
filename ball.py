from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.speed_up = 0.03

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed_up *= 0.90

    def reset_position(self):
        self.goto(0, 0)
        self.speed_up = 0.03
        self.bounce_x()
