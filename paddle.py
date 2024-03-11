from turtle import Turtle

R_PADDLE =  (350, 0)
L_PADDLE = (-350, 0)

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1) # 100x20 paddle size
        self.setposition(position)

        
    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y = new_y)


    def go_down(self):
        if self.ycor() > -235:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y = new_y)
