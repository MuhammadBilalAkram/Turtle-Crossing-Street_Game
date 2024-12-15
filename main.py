import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

new_player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(new_player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    #detect colision with car
    for car in car_manager.all_cars:
        if car.distance(new_player)<20:
            game_is_on = False
            scoreboard.game_over()
    #detect successful crossing
    if new_player.is_at_finish_line():
        new_player.go_to_start()
        car_manager.level_up()
        scoreboard.increas_level()
        scoreboard.update_scoreboard()



screen.exitonclick()
