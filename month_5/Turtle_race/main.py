# Import the turtle module
from turtle import Turtle, Screen
# Create the turtle object 'tim' from the class 'Turtle'
tim = Turtle()
screen = Screen()
tim.shapesize(5)
tim.pensize(3)
# Move tim forwards - draw a line in the forward direction
def move_forwards():
    tim.forward(10)
# Move time backwards - draw a line in the backward direction
def move_backwards():
    tim.backward(10)
# Turn tim to the left by 10 degrees
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
#Turn tim to the right by 10 degrees
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
# Clear the screen.
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
# Get the screen in a listening mode for an event.
screen.listen()
#Specify the events and parse a higher order function that will only execute when the event happens.
# Note: Higher order functions are absent parenthesis.
# They are only triggered for execution when that specific event happens.
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()