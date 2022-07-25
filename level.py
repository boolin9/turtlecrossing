from turtle import Turtle
from player import Player


class Level(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.level_num = 0
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-230,260)
        self.write(f"Level: {self.level_num}", align="center", font=("Bit5x3", 30, "normal")) 
        self.draw_line((-300, 245))
        self.draw_line((-300, -245)) 
        
    
    def draw_line(self, coordinates):
        self.goto(coordinates)
        for _ in range(30):
            self.pd()
            self.fd(10)
            self.pu()
            self.fd(10)
            
    
    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Bit5x3", 40, "normal"))