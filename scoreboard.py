from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    """Models the scoreboard to keep track of the status of the game."""
    score = 0
    highest_score = 0

    def __init__(self):
        super().__init__()
        self.get_highest_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def increase_score(self):
        """Increases the player's score by 1."""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard's message."""
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highest_score:
            self.set_highest_score()
        self.score = 0
        self.update_scoreboard()

    def get_highest_score(self):
        with open("data.txt") as data:
            score = data.read()

        self.highest_score = int(score)

    def set_highest_score(self):
        self.highest_score = self.score
        with open("data.txt", "w") as data:
            data.write(str(self.highest_score))
