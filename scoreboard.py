from turtle import Turtle
from config import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        
        self.draw_safe_zones()
        self.update_scoreboard()

    def draw_safe_zones(self):
        painter = Turtle()
        painter.hideturtle()
        painter.color("white")
        painter.penup()
        painter.pensize(2)
        
        painter.goto(-300, -260)
        painter.pendown()
        painter.goto(300, -260)
        
        painter.penup()
        painter.goto(-300, 260)
        painter.pendown()
        painter.goto(300, 260)

    def update_scoreboard(self):
        self.clear()
    
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
        self.goto(0, -40)
        self.write("Press 'R' to Restart", align="center", font=("Courier", 14, "normal"))

    def reset_score(self):
        self.level = 1
        self.clear() 
        self.update_scoreboard()