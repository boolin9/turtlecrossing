from turtle import Turtle


class Player(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.setheading(90)
        self.color('green')
        self.shape('turtle')
        self.goto(0, -270)
        
    
    def up(self):
        self.setheading(90)
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
                
                
    def down(self):
        self.setheading(270)
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
        
    def left(self):
        self.setheading(180)
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
                
                
    def right(self):
        self.setheading(0)
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())