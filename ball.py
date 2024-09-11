from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        # initialize the ball
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.speed_up = 0.03

    # define the movement
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # move to the opposite direction in the y-axis when hit the bottom or the top
    def bounce_y(self):
        self.y_move *= -1

    # move to the opposite direction in the x-axis when hit one of the paddles
    def bounce_x(self):
        self.x_move *= -1
        self.speed_up *= 0.90

    # reset the position of the ball
    def reset_position(self):
        self.goto(0, 0)
        self.speed_up = 0.03
        self.bounce_x()
