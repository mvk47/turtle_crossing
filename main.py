from turtle import Screen
from turtle_car import Vehicle
from car import CarManager
# import random
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Turtle crossing")
screen.setup(height=720, width=1080)
screen.bgcolor("black")
screen.tracer(0)
vehicle = Vehicle()
car_manager = CarManager()
score = ScoreBoard()

screen.listen()
game_is_on = True
while game_is_on:
    screen.onkey(vehicle.up, "Up")
    time.sleep(.03)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision of car and turtle

    for car in car_manager.all_cars:
        if car.distance(vehicle) < 23:
            game_is_on = False
            score.game_over()

    if vehicle.ycor() > 300:
        vehicle.go_to_start()
        car_manager.level_up()
        score.score_update()
screen.exitonclick()
