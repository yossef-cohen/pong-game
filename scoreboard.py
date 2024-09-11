from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_core = 0
        self.r_core = 0
        self.goto(-100, 200)
        self.write(self.l_core, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_core, align="center", font=("courier", 80, "normal"))

    def l_point(self):
        self.l_core += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_core += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_core, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_core, align="center", font=("courier", 80, "normal"))