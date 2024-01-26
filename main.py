import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")
screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Collision with wall
    if (snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290
            or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290):
        scoreboard.reset_score()
        snake.reset()

    # Collision with tail
    for segment in snake.snake[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()

screen.exitonclick()
