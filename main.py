from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
s = Snake()
f = Food()
score_board = Score()
screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

game_on = True
print(game_on)
while game_on:
    s.alive()
    screen.update()
    time.sleep(0.1)
    s.move()
    if f.distance(s.head) <= 15:
        score_board.increment()
        f.food_move()
        s.add_new_seg()
        print(score_board.counter)

score_board.game_over()

screen.exitonclick()





