from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    """Models the snake, and controls its length and movement."""
    snake = []

    def __init__(self):
        self.create_snake()
        self.snake_head = self.snake[0]

    def add_segment(self, position):
        """Creates a new Turtle instance and appends it at the
        position given as a new segment."""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def create_snake(self):
        """Adds the initial segments for the snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend_snake(self):
        """Calculates the current last segment of the snake and
        appends a new segment at the very end to extend it."""
        last_pos = self.snake[-1].position()
        self.add_segment(last_pos)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)

        self.snake.clear()
        self.create_snake()
        self.snake_head = self.snake[0]

    def move(self):
        """Moves all segments of the snake following its current direction."""
        # The range starts from the last segment of the snake up to position 1
        # This takes every segment of the snake minus the first
        # and swaps its placement with the immediately following one
        # to solve the issue of snake mobility even when turning
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)

        # Then we move forward the head of the snake
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """Sets the snake's direction to Up"""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """Sets the snake's direction to Down"""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        """Sets the snake's direction to Right"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        """Sets the snake's direction to Left"""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
