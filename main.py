from turtle import Screen
import snake
import time
import food

# define screen object attributes
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)
scr.listen()

# create snake instance
ekans = snake.Snake()
# create good instance
food = food.Food()

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


# only exit the screen on click of mouse - keeps window visible
scr.exitonclick()
