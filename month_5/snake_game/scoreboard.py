from locale import normalize
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.write(f"score: {self.score}", align="center", font=("Arial", 24, "normal"))
