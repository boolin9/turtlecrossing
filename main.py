from turtle import Screen
from level import Level
from player import Player
from car import Car
import time


screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

level = Level()
player = Player()
car = Car()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

game_on = True

while game_on:
    screen.update()
    # time.sleep(car.move_speed) <- car speed
    
    if player.distance(car) < 11:
        level.game_over()
        game_on = False
        
    if player.ycor() > 270:
        level.level_num += 1
        level.update_scoreboard()
        player.goto(0, -270)
        # time.sleep(car.increase_speed) <- increase car speed


screen.exitonclick()