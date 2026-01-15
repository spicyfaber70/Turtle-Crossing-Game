from turtle import Turtle
from config import *
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # 1/6 chance to spawn a car
        if random.randint(1, SPAWN_CHANCE) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            
            # spawn at the right edge but only in specific lanes
            spawn_y = random.choice(LANES)
            new_car.goto(300, spawn_y)
            
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def cleanup_traffic(self):
        #prevents memory leaks by removing cars that have driven off the left side

        for car in self.all_cars:
            if car.xcor() < -320:
                car.hideturtle()
        
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        
    def reset_manager(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE