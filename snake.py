from turtle import Turtle

# CONSTANTS -START ###
MOVE_DISTANCE = 20
#TURN_ANGLE = 90
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# CONSTANTS -END ###


class Snake:

    def __init__(self):
        # create a list for the snake body
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        # create three Turtle objects
        # each Turtle should be a white square (default size:20x20)
        for body_index in range(0, 3):
            body_part = Turtle(shape="square")
            body_part.color("white")
            body_part.penup()
            body_part.goto(0 - (body_index * 20), 0)
            self.snake_body.append(body_part)

    def move_forward(self):
        """
        To move forward we are starting from the last body segment of the snake
        Getting the coordinate of the one in front of it and moving it to that one's position.
        However, we only do this for body segment that are not the head.
        The head will continue to move forward
        :return:
        """
        # loop using range and in reverse
        for seg_num in range(len(self.snake_body) - 1, -1, -1):  # range format for stepping range(start, stop, step)
            # if the segment in the loop cycle is not the head then move this segment to the position
            # of the segment that's in front of it
            if seg_num != 0:
                segment_in_front_pos = self.snake_body[seg_num - 1].pos()
                self.snake_body[seg_num].goto(segment_in_front_pos)
            # when the loop cycle reaches the head, the head is just meant to move forward
            else:
                self.snake_body[seg_num].forward(MOVE_DISTANCE)

    def turn_left(self):
        """
        Turns the head of the snake body to the left direction (180 Turtle Degrees)
        :return:
        """
        if self.snake_body[0].heading() == UP or self.snake_body[0].heading() == DOWN:
            self.snake_body[0].setheading(LEFT)

    def turn_right(self):
        """
        Turns the head of the snake body to the right direction (0 Turtle Degrees)
        :return:
        """
        if self.snake_body[0].heading() == UP or self.snake_body[0].heading() == DOWN:
            self.snake_body[0].setheading(RIGHT)

    def turn_up(self):
        """
        Turns the head of the snake body to the up direction (90 Turtle Degrees)
        :return:
        """
        if self.snake_body[0].heading() == LEFT or self.snake_body[0].heading() == RIGHT:
            self.snake_body[0].setheading(UP)


    def turn_down(self):
        """
        Turns the head of the snake body to the down direction (270 Turtle Degrees)
        :return:
        """
        if self.snake_body[0].heading() == LEFT or self.snake_body[0].heading() == RIGHT:
            self.snake_body[0].setheading(DOWN)
