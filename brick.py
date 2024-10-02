import random
from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(self.random_color())  # Set a random color for the brick
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=1, stretch_len=3)  # Adjust size as needed

    def random_color(self):
        """Generate a random color in RGB format."""
        return (random.random(), random.random(), random.random())

    def destroy(self):
        self.hideturtle()  # Hide the brick when destroyed
