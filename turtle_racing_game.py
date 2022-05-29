import time
import random
from turtle import Turtle
from turtle import Screen

def turtles_on_start():
    x = -350
    y = 100
    turtles = []
    colors = ['magenta', 'blue', 'green', 'yellow', 'orange', 'red']
    for color in colors:
        turtle = Turtle()
        turtle.shape('turtle')
        turtle.penup()
        turtle.color(color)
        turtle.goto(x, y)
        turtles.append(turtle)
        y -= 40

    return turtles

def begin_race(turtles):
    steps = [8, 12, 16, 20, 24, 28]
    distances = [0,0,0,0,0,0]
    while True:
        for i, turtle in enumerate(turtles):
            step = random.choice(steps)
            distances[i] += step
            turtle.forward(step)
            if distances[i] >= 700:
                return turtle.color()[0]

def finish_the_game(result, bet):
    if result == bet:
        print(f'You found. The {result} turtle is the winner!')
    else:
        print(f'You loss. The {result} turtle is the winner!')

def game():
    screen = Screen()
    bet = screen.textinput('Make your bet', 'Who will win the race? Enter a color\n'
                                            '(magenta/blue/green/yellow/orange/red): ')

    turtles = turtles_on_start()
    result = begin_race(turtles)
    finish_the_game(result = result, bet = bet)
    time.sleep(2)
    screen.bye()
    time.sleep(2)
    #screen.exitonclick()
game()