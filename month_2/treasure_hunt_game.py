#TREASURE HUNT GAME

print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* 
""")

#Version 1 of the game

print("Welcome to Treasure island. \n Your mission is to find the treasure")

destination = input("Choose where to go, Left or Right?:  ")
destination = destination.lower()
if destination == "left":
	water = input("Swim or Wait?:  ")
	water = water.lower()
	if water == "wait":
		door = input("Which door? red, blue or yellow?:  ")
		door = door.lower()
		if door == "yellow":
			print("Hurray! You win!")
		elif (door == "red") or (door == "blue"):
			print("Game over!")
	else:
		print("Game over!")
else:
	print("Game over!")
	
print("Welcome to Treasure island.")
	
print("Your mission is to find the treasure")


#-------------------------------
# Improved version of the game.
#-------------------------------

# \-backward slash is used to escape ' ' or " " issues.
# If you have the case where you have to use both " " and ' ', make sure to use ' ' first and then " " inside ' '.

#-------uncomment the code below to test it---------

# choice1 = input('You\'re at a crossroad, where do you want to go? "left" or "right" \n').lower()
# if choice1 == "left":
# 	choice2 = input('You\'ve come to a lake. There\'s and island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n ' ).lower()
# 	if choice2 == "wait":
# 		choice3 = input('You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which door do you want to choose?\n ').lower()
# 		if choice3 == "yellow":
# 			print("You found the treasure! You Win!")
# 		elif choice3 == "blue":
# 			print("You enter a room of beasts. Game Over")
# 		else:
# 				print("You chose a door that doesn't exist. Gave Over!")
# 	else:
# 		print(" You got attacked by a trout. Game over!")
# else:
# 	print("You fell into a hole. Game Over!")

