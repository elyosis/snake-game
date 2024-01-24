from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    """Models the scoreboard to keep track of the status of the game."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def increase_score(self):
        """Increases the player's score by 1."""
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard's message."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def end_game(self):
        """Sets a Game Over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)