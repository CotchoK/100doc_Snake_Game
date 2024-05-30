from turtle import Screen, Turtle
import time

# define screen object attributes
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)
scr.listen()

# create a list for the snake body
snake_body = []

def move_forward():
    """
    To move forward we are starting from the last body segment of the snake
    Getting the coordinate of the one in front of it and moving it to that one's position.
    However we only do this for body segment that are not the head.
    The head will continue to move forward
    :return:
    """
    # loop using range and in reverse
    for seg_num in range(len(snake_body) - 1, -1, -1):  # range format for stepping range(start, stop, step)
        # if the segment in the loop cycle is not the head then move this segment to the position
        # of the segment that's in front of it
        if seg_num != 0:
            segment_in_front_pos = snake_body[seg_num - 1].pos()
            snake_body[seg_num].goto(segment_in_front_pos)
        # when the loop cycle reaches the head, the head is just meant to move forward
        else:
            snake_body[seg_num].forward(20)


def turn_left():
    """
    Turns the head of the snake body left 90 degrees
    :return:
    """
    snake_body[0].setheading(snake_body[0].heading() + 90)


def turn_right():
    """
    Turns the head of the snake body right 90 degrees
    :return:
    """
    snake_body[0].setheading(snake_body[0].heading() - 90)


# create three Turtle objects
# each Turtle should be a white square (default size:20x20)
for body_index in range(0, 3):
    body_part = Turtle(shape="square")
    body_part.color("white")
    body_part.penup()
    body_part.goto(0 - (body_index * 20), 0)
    snake_body.append(body_part)

game_over = False

# game loop
while not game_over:
    scr.onkey(turn_left, "a")
    scr.onkey(turn_right, "d")
    move_forward()
    scr.update()
    time.sleep(0.2)




# only exit the screen on click of mouse - keeps window visible
scr.exitonclick()
