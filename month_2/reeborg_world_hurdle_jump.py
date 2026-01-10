# # This program instructs the robot in reeborg's world to make a particular number of jumps during a hurdle
# # Visit:https://reeborg.ca/reeborg.html test the code.

# #---------------------------------------------------------------------
# #Method 1
# #----------------------------------------------------------------------

# # Define the turn_right() function
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
        

# # Using a for-loop for the jumps 
# for square in range(3):
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# #---------------------------------------------------------------------
# #Method 2
# #----------------------------------------------------------------------

# # Define the turn_right() function
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# #Using a function for the jumps
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# jump()
# jump()
# jump()

# #---------------------------------------------------------------------
# #Method 3
# #----------------------------------------------------------------------
    
# # Define the turn_right() function
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# #Using a function for the jumps
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# # for-loop to perform the jump() function 3 times

# for step in range(3):
#     jump()


# #---------------------------------------------------------------------
# #Method 4---Using a while loop for the program
# #----------------------------------------------------------------------

# Define the turn_right() function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Using a function for the jumps
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# while-loop to perform the jump() function 3 times

number_of_hurdles = 3
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

# #---------------------------------------------------------------------
# #Method 4---Using while-loop with the at_goal() function to stop the robot whenever it finds a flag
# #----------------------------------------------------------------------

# # Define the turn_right() function
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# #Using a function for the jumps
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# # while-loop to perform the jump() function 3 times


# while not at_goal():
#     jump()