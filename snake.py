import random
from turtle import Turtle, Screen
import time
from score import Score

MOVE_DISTANCE = 10
START_POSITIONS = [(-10, 0), (-20, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.head = Turtle('circle')
        self.head.shapesize(0.5, 0.5)
        self.head.penup()
        self.head.color('gray')
        self.head.setpos(0, 0)
        self.segments.append(self.head)
        for i in range(2):
            self.t = Turtle('square')
            self.t.shapesize(0.5, 0.5)
            self.t.penup()
            self.t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.t.setpos(START_POSITIONS[i])
            self.segments.append(self.t)

    def add_new_seg(self):
        new_t = Turtle('square')
        new_t.shapesize(0.5, 0.5)
        new_t.penup()
        pos = self.segments[len(self.segments) - 1].pos()
        new_t.setpos(pos)
        new_t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.segments.append(new_t)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def alive(self):
        # for loop using slicing: for i in range(self.segments[1:]):
        for i in range(2, len(self.segments), 1):
            if self.head.distance(self.segments[i]) < 5 or self.head.xcor() == 300 or \
                    self.head.xcor() == -300 or self.head.ycor() == 300 or self.head.ycor() == -300:
                sc = Score()
                sc.game_over()
                time.sleep(3)
                exit()








