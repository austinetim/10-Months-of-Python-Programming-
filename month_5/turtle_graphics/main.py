from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle") # This is an attribute
tim.color("red")

# DRAWING A SQUARE

# for _ in range(4):
#     tim.forward(100)  # This is a method
#     tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# DRAWING DASHED LINES

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#DRAWING A TRIANGLE, SQUARE,

# TRIANGLE
tim.forward(100)
tim.right(120)
tim.forward(100)
tim.right(120)
tim.forward(100)

#SQUARE
tim.right(120)
for _ in range(4):
    tim.forward(100)  # This is a method
    tim.right(90)

# PENTAGON
tim.forward(100)
for _ in range(4):
    tim.right(72)
    tim.forward(100)

# tim.right(72)
# tim.forward(100)
# tim.right(72)
# tim.forward(100)
# tim.right(72)
# tim.forward(100)
# tim.right(72)
# tim.forward(100)

#HEXAGON
tim.right(72)
tim.forward(100)
for _ in range(5):
    tim.right(60)
    tim.forward(100)




















screen = Screen()
screen.exitonclick()