from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh_location()


    def refresh_location(self):
        random_x = round(random.randint(-280, 280) / 20) * 20
        random_y = round(random.randint(-280, 280) / 20) * 20
        self.goto(random_x, random_y)