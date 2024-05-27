from turtle import Screen, Turtle

# define screen object attributes
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")


# create a list for the snake body
snake_body = []
# create three Turtle objects
# each Turtle should be a white square (default size:20x20)
for body_index in range(0, 3):
    body_part = Turtle(shape="square")
    body_part.color("white")
    body_part.penup()
    body_part.goto(0 - (body_index * 20), 0)
    snake_body.append(body_part)




scr.exitonclick()
