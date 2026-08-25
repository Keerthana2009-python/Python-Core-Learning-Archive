import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    #Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 13:
            game_is_on = False
            scoreboard.game_over()
    #Detect turtle reaching other side
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()


screen.exitonclick()