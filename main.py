from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#creating the screen
screen= Screen()
snake = Snake()
food = Food()
score = ScoreBoard()
#configuering the screen
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

#controlling the snake with keyboard
game_over = True
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.turn_right,key="Right")
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.listen()


while game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.append_segment()
    #wall collosion
    # checking wether the game is over.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_over = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = False
            score.game_over()






screen.exitonclick()