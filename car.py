from turtle import Turtle, color
import random

COLORS = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']
START_MOVE_DIST = 5


class Car(Turtle):
    
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = START_MOVE_DIST
        
        
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:    
            new_car = Turtle()
            new_car.goto(0,0)
            new_car.shape('square')
            new_car.pu()
            new_car.shapesize(1, 2)        
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-232, 232)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    
    def increase_speed(self):
        self.car_speed += 2
            