import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle") # This is an attribute
tim.color("red")


# MAKING RANDOM WALKS

#Set up our lists of choices
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270] # East, North, West, South
tim.pensize(5)
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(300):
    # set the color randomly
    tim.color(random_color())
    #set the angle randomly
    current_angle = random.choice(directions)
    tim.setheading(current_angle)

    # move forward
    tim.forward(30)




screen = Screen()
screen.exitonclick()