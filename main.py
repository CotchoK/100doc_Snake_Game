from turtle import Screen
import snake
import time

# define screen object attributes
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)
scr.listen()

# create snake instances
ekans = snake.Snake()

# define the game_over state as False
game_over = False

# game loop - while game loop is not false then continue to loop
while not game_over:
    # user interactions
    scr.onkey(ekans.turn_left, "a")
    scr.onkey(ekans.turn_right, "d")

    ekans.move_forward()
    scr.update()
    time.sleep(0.1)


# only exit the screen on click of mouse - keeps window visible
scr.exitonclick()
