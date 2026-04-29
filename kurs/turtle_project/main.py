from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

timmy.color('purple')
timmy.pencolor('purple')

def square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)
    screen.exitonclick()

screen = Screen()

square()
