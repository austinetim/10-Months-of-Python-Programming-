# import turtle
# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# tim.shape("turtle") # This is an attribute
# tim.color("red")
#
# # DRAWING A SQUARE
#
# # for _ in range(4):
# #     tim.forward(100)  # This is a method
# #     tim.right(90)
# # tim.forward(100)
# # tim.right(90)
# # tim.forward(100)
# # tim.right(90)
# # tim.forward(100)
#
# # DRAWING DASHED LINES
#
# # for _ in range(15):
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
#
# #DRAWING A TRIANGLE, SQUARE,
#
# # # TRIANGLE
# # tim.pensize(5)
# # tim.pencolor("black")
# # tim.forward(100)
# # tim.right(120)
# # tim.forward(100)
# # tim.right(120)
# # tim.forward(100)
# #
# # #SQUARE
# # tim.right(120)
# # for _ in range(4):
# #     tim.pencolor("red")
# #     tim.forward(100)  # This is a method
# #     tim.right(90)
# #
# # # PENTAGON
# # tim.forward(100)
# # for _ in range(4):
# #     tim.pencolor("blue")
# #     tim.right(72)
# #     tim.forward(100)
# #
# # # tim.right(72)
# # # tim.forward(100)
# # # tim.right(72)
# # # tim.forward(100)
# # # tim.right(72)
# # # tim.forward(100)
# # # tim.right(72)
# # # tim.forward(100)
# #
# # #HEXAGON
# # tim.right(72)
# # tim.forward(100)
# # for _ in range(5):
# #     tim.pencolor("yellow")
# #     tim.right(60)
# #     tim.forward(100)
# #  # HEPTAGON
# # tim.right(60)
# # tim.forward(100)
# # for _ in range(6):
# #     tim.pencolor("purple")
# #     tim.right(51.42857142857143)
# #     tim.forward(100)
# #
# #  # OCTAGON
# # tim.right(51.42857142857143)
# # tim.forward(100)
# # for _ in range(7):
# #     tim.pencolor("brown")
# #     tim.right(45)
# #     tim.forward(100)
# #
# #  # NONAGON
# # tim.right(45)
# # tim.forward(100)
# # for _ in range(8):
# #     tim.pencolor("orange")
# #     tim.right(40)
# #     tim.forward(100)
# #
# #  # OCTAGON
# # tim.right(40)
# # tim.forward(100)
# # for _ in range(9):
# #     tim.pencolor("indigo")
# #     tim.right(36)
# #     tim.forward(100)
#
#
# # # A BETTER WAY OF SOLVING THE CHALLENGE: DRAWING THE 3-10 SIDED POLYGON.
# # # Function to Draw the number of sides
# # line_color = ["midnight blue", "dark slate blue", "indigo", "purple", "dark green",
# #               "medium spring green", "dodger blue", "pale violet red"]
# # tim.pensize(5)
# # def draw_shape(number_of_sides):
# #     angle = 360/number_of_sides
# #     for _ in range(number_of_sides):
# #         tim.forward(100)
# #         tim.right(angle)
# #
# # # Loop to iterate through from 3 sided polygon to 10 sided polygon
# # for shape_sides in range(3, 11):
# #     tim.color(random.choice(line_color))
# #     draw_shape(shape_sides)
#
#
# # MAKING RANDOM WALKS
#
# #Set up our lists of choices
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270] # East, North, West, South
# tim.pensize(5)
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# for _ in range(300):
#     # set the color randomly
#     tim.color(random_color())
#     #set the angle randomly
#     current_angle = random.choice(directions)
#     tim.setheading(current_angle)
#
#     # move forward
#     tim.forward(30)
#
#
#
#
#
#
# screen = Screen()
# screen.exitonclick()