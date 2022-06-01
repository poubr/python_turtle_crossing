from turtle import Screen, Turtle
from player import Player
from cars import Car
from level import Level
import time

# Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Why Did The Turtle Cross The Road")
screen.bgcolor('MistyRose')
screen.listen()
screen.tracer(0)

# Drawing road boundaries:
draw_road = Turtle()
draw_road.color('thistle4')
draw_road.penup()
draw_road.goto(-320, 220)
draw_road.pendown()
draw_road.pensize(10)
draw_road.forward(640)
draw_road.right(90)
draw_road.forward(440)
draw_road.right(90)
draw_road.forward(640)

# Creating level check:
level = Level()

# Creating player's turtle and setting up controls:
player = Player()

screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')
screen.onkey(player.go_right, 'Right')
screen.onkey(player.go_left, 'Left')

# Creating list of car objects (so far empy)
wroom_wroom_machines = Car()


# Actual game:
def turtle_crossing():
    sleep_increment = 0.1
    game_on = True
    while game_on:
        screen.update()
        time.sleep(sleep_increment)
        # Populating and moving the car list with cars:
        wroom_wroom_machines.create_cars()
        wroom_wroom_machines.move()

        # Detecting player successfully crossing:
        if player.ycor() >= 230:
            player.reset()
            level.current_level += 1
            level.write_level()
            wroom_wroom_machines.chance -= 1
            sleep_increment *= 0.7

        # Detecting turtle - car collision:
        for wroom in wroom_wroom_machines.all_cars:
            if wroom.distance(player) < 20:
                level.game_over_text()
                game_on = False


if __name__ == '__main__':
    turtle_crossing()

screen.exitonclick()
