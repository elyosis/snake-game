from turtle import Turtle
from random import randint


class Food(Turtle):
    """Models the food for the snake."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("DeepPink2")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        """Sets a new random position for the food."""
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
