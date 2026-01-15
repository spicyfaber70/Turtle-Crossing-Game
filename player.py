from turtle import Turtle
from config import *

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(PLAYER_COLOR)
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def has_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False