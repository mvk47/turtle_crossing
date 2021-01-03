from turtle import Turtle
import random

COLORS = ["blue", "yellow", "green", "orange"]
DISTANCE = 2
INCREMENT = 2


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = DISTANCE
        
    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.y = random.randint(-250, 250)
            new_car.shapesize(stretch_len=3, stretch_wid=1)
            new_car.color("blue")
            new_car.penup()
            new_car.goto(300, new_car.y)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREMENT
