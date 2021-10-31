from turtle import Turtle
ALIGNMENT = "center"
FONT = "courier"


class Score(Turtle):
    counter = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def new_text(self, new_str, new_pos):
        self.shapesize(0.5)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setpos(new_pos)
        self.write(f"{new_str} {self.counter}", False, ALIGNMENT, font=(FONT, 14, 'normal'))

    def increment(self):
        self.counter += 1
        self.reset()
        self.new_text("Score: ", (0, 280))

    def game_over(self):
        self.shapesize(0.5)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setpos(0, 0)
        self.color('red')
        self.write("Game Over!", False, ALIGNMENT, font=(FONT, 16, 'normal'))


