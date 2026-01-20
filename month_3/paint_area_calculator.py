# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paints you'll need to buy.

import math
def paint_calc(height, width, coverage):
    # number_of_cans = round((height * width) / coverage)
    # This is also right: To use the method below, uncomment the import math line.
    number_of_cans = math.ceil((height * width)/coverage)

    #Print the result
    print(f"You'll need {number_of_cans} cans of paint")

# The code will take note of all the variables below before the function call.
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage_val = 5
paint_calc(height = test_h, width = test_w, coverage = coverage_val)

