
# scoreboard.py
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0  # Initialize score
        self.title_art = [
            " ____                 _               _   ",
            "| __ ) _ __ ___  __ _| | _____  _   _| |_ ",
            "|  _ \\| '__/ _ \\/ _` | |/ / _ \\| | | | __|",
            "| |_) | | |  __/ (_| |   < (_) | |_| | |_ ",
            "|____/|_|  \\___|\\__,_|_|\\_\\___/ \\__,_|\\__|"
        ]
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.display_ascii_art()
        self.goto(300, 260)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "bold"))
        self.goto(260, 240)
        self.write("Controls: A(Left), D(Right)", align="center", font=("Courier", 12, "bold"))
        self.goto(250, 210)
        self.write("Break Free,Smash Limits!!!", align="center", font=("Courier", 14, "bold"))

    def add_score(self, points=1):  # Method to add score
        self.score += points
        self.update_scoreboard()

    def display_ascii_art(self):
        x_position = -380  # Adjust this for your screen width
        y_position = 294  # Start from near the top of the screen

        for line in self.title_art:
            self.goto(x_position, y_position)
            self.write(line, align="left", font=("Courier", 8, "bold"))
            y_position -= 20  # Move down for the next line

