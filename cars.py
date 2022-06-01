from turtle import Turtle
from random import choice

COLORS = ['cyan3', 'DarkOrchid1', 'DarkOrange2', 'aquamarine3', 'DeepSkyBlue4', 'purple3', 'PaleGreen4', 'PaleGreen2']
X_COORS = [x for x in range(300, 350)]
Y_COORS = [y for y in range(-200, 200)]


class Car:
    def __init__(self):
        self.all_cars = []
        self.chance = 15

    def create_cars(self):
        if choice([i for i in range(self.chance)]) == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.goto(choice(X_COORS), choice(Y_COORS))
            car.seth(180)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(20)
