from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}", move=False, font=FONT, align=ALIGNMENT)

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
