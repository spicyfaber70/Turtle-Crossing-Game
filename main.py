import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from config import *

class GameController:
    def __init__(self):
        self.screen = Screen()
        self._setup_screen()
        
        self.player = Player()
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard()
        
        self.is_running = True
        self.is_game_over = False

    def _setup_screen(self):
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title(TITLE)
        self.screen.tracer(0)
        self.screen.listen()

    def _setup_inputs(self):
        self.screen.onkeypress(self.player.move_up, "Up")
        self.screen.onkeypress(self.restart_game, "r")
        self.screen.onkeypress(self.quit_game, "Escape")

    def restart_game(self):
        if self.is_game_over:
            self.is_game_over = False
            self.player.reset_position()
            self.car_manager.reset_manager()
            self.scoreboard.reset_score()

    def quit_game(self):
        self.is_running = False

    def run(self):
        self._setup_inputs()

        while self.is_running:
            time.sleep(0.1)
            self.screen.update()

            if not self.is_game_over:
                # 1) manage traffic
                self.car_manager.create_car()
                self.car_manager.move_cars()
                self.car_manager.cleanup_traffic() # memory Leak Fix

                # 2) collision detection
                for car in self.car_manager.all_cars:
                    if car.distance(self.player) < 20:
                        self.is_game_over = True
                        self.scoreboard.game_over()

                # 3) level Up
                if self.player.has_finished():
                    self.player.reset_position()
                    self.car_manager.level_up()
                    self.scoreboard.increase_level()

        self.screen.exitonclick()

if __name__ == "__main__":
    game = GameController()
    game.run()