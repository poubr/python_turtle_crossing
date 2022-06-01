from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('VioletRed4')
        self.penup()
        self.seth(90)
        self.goto(0, -270)

    def reset(self):
        self.goto(0, -270)

    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-20)

    def go_right(self):
        self.goto(self.xcor()+20, self.ycor())

    def go_left(self):
        self.goto(self.xcor()-20, self.ycor())

