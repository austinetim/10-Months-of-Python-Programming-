# Creating a class --- the blueprint
class User:
    pass

#Creating an object from the blueprint
user_1 = User()

#Adding attributes --- variable associated with an object

user_1.id = "001"
user_1.username = "Clement"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Tim"

# CONSTRUCTORS
# --- They allow us to specify what should happen when our objects is being created.
