from turtle import Screen
from level import Level
from player import Player
from car import START_MOVE_DIST, Car
import time

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

level = Level()
player = Player()
cars = Car()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    
    cars.create_car()
    cars.move_cars()
    
    for car in cars.all_cars:
        if car.distance(player) < 18:
            level.game_over()
            game_on = False
        
    if player.ycor() > 270:
        level.level_num += 1
        level.update_scoreboard()
        player.goto(0, -270)
        cars.increase_speed()
        

screen.exitonclick()