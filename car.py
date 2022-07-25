from turtle import Turtle, color
import random

COLORS = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']


class Car(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.shape('square')
        self.shapesize(1, 2)        
        self.color(random.choice(COLORS))
        self.move_speed = 0.08