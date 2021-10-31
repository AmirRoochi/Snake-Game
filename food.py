from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("pink")
        self.goto(0, 80)

    def food_move(self):
        self.setpos(random.randint(-280, 280), random.randint(-280, 280))



