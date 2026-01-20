# This function only takes one input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet_with_name("Paul") #--we supply the input when we call the function

Something      =     123
#  |                  |
# Parameter         Argument

# This function takes two inputs
# It also uses positional arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}?")
greet_with("Paul", "Nigeria") 

# If we exchanged the argument positions, the function by default uses positional arguments to assign the arguments to the parameters in the function defini.tion
 

# Functions with keyword arguments

def greet_with(name, position):
    print(f"Hello {name}")
    print(f"How is it like to be in {position}")
greet_with(position = "Nigeria", name = "Paul")