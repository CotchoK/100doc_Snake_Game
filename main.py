from turtle import Screen
import snake
import time
import food
import scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# define screen object attributes
scr = Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)
scr.listen()

# create snake instance
ekans = snake.Snake()
# create good instance
food = food.Food()
#create scoreboard instance
scoreboard = scoreboard.Scoreboard()

# user interactions - using up, down, left, right
scr.onkey(ekans.turn_up, "Up")
scr.onkey(ekans.turn_down, "Down")
scr.onkey(ekans.turn_left, "Left")
scr.onkey(ekans.turn_right, "Right")

# define the game_over state as False
game_over = False

# game loop - while game loop is not false then continue to loop
while not game_over:
    scr.update()
    time.sleep(0.1)
    ekans.move_forward()

    # Detect collision with snake head and food
    if ekans.snake_body[0].distance(food) < 15:
        food.refresh_location()
        scoreboard.refresh_score()

    # Detect collision with snake head and wall
    if (ekans.snake_body[0].xcor() < -(SCREEN_WIDTH / 2) + 20 or
            ekans.snake_body[0].xcor() > (SCREEN_WIDTH / 2) - 20 or
            ekans.snake_body[0].ycor() < -(SCREEN_HEIGHT / 2) + 20 or
            ekans.snake_body[0].ycor() > (SCREEN_HEIGHT / 2) - 20
    ):
        game_over = True

scoreboard.game_over()


# only exit the screen on click of mouse - keeps window visible
scr.exitonclick()
