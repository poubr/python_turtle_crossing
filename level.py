from turtle import Turtle

FONT = ('Helvetica', 30, 'normal')


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color('VioletRed4')
        self.penup()
        self.hideturtle()
        self.goto(-260, 250)
        self.current_level = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(-260, 250)
        self.write(arg=f"Level {self.current_level}", move=False, align='left', font=FONT)

    def game_over_text(self):
        self.goto(-90, 50)
        self.write(arg=f"GAME OVER", move=False, align='left', font=FONT)
        self.goto(-150, 0)
        self.write(arg=f"You killed your turtle (ಥ⌣ಥ)", move=False, align='left', font=FONT)


