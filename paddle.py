# paddle.py
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)  # Adjust width for paddle
        self.penup()
        self.goto(position)

    def go_left(self):
        if self.xcor() > -350:  # Prevent paddle from going off the left edge
            new_x = self.xcor() - 30
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 350:  # Prevent paddle from going off the right edge
            new_x = self.xcor() + 30
            self.goto(new_x, self.ycor())
