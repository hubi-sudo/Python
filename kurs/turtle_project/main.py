from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.shape("turtle")

timmy.color('purple')
timmy.pencolor('purple')

def square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)
    screen.exitonclick()


def dashed_line():
    for i in range(50):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


colors = ["red", "green", "blue", "violet", "brown", "black", "purple", "orange"]

def shapes():
    angles = 3
    while angles < 10:
        timmy.pencolor(choice(colors))
        for i in range(3, 3+ angles):
            timmy.forward(100)
            timmy.right(360/angles)
        angles += 1
    screen.exitonclick()

angles = [0, 90, 180, 270]

def random_walk():
    timmy.width(20)
    timmy.speed(6)
    for i in range (100):
        timmy.pencolor(choice(colors))
        timmy.forward(50)
        timmy.right(choice(angles))
    screen.exitonclick()



screen = Screen()

#square()

#dashed_line()

#shapes()

random_walk()