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
tim.pensize(5)
tim.pencolor("black")
tim.forward(100)
tim.right(120)
tim.forward(100)
tim.right(120)
tim.forward(100)

#SQUARE
tim.right(120)
for _ in range(4):
    tim.pencolor("red")
    tim.forward(100)  # This is a method
    tim.right(90)

# PENTAGON
tim.forward(100)
for _ in range(4):
    tim.pencolor("blue")
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
    tim.pencolor("yellow")
    tim.right(60)
    tim.forward(100)
 # HEPTAGON
tim.right(60)
tim.forward(100)
for _ in range(6):
    tim.pencolor("purple")
    tim.right(51.42857142857143)
    tim.forward(100)

 # OCTAGON
tim.right(51.42857142857143)
tim.forward(100)
for _ in range(7):
    tim.pencolor("brown")
    tim.right(45)
    tim.forward(100)

 # NONAGON
tim.right(45)
tim.forward(100)
for _ in range(8):
    tim.pencolor("orange")
    tim.right(40)
    tim.forward(100)

 # OCTAGON
tim.right(40)
tim.forward(100)
for _ in range(9):
    tim.pencolor("indigo")
    tim.right(36)
    tim.forward(100)




















screen = Screen()
screen.exitonclick()