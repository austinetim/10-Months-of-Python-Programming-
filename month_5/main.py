# Creating a class --- the blueprint
class User:
         def __init__(self, user_id, username):
             self.id = user_id
             self.username = username
             self.followers = 0 # This is a default value. It does not need to be specified when the object is being created.

#Creating an object from the blueprint
user_1 = User("001", "Clement")
user_2 = User("002", "Timothy")
print(user_1.id, user_1.username)


#Adding attributes --- variable associated with an object
# Without initialization:

# user_1.id = "001"
# user_1.username = "Clement"
# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Tim"
# print(user_2.username)
