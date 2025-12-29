#This program checks for the rollercoaster ride eligibility using the height of the user.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?  "))
bill = 0
if height > 120:
	print("You can ride the rollercoaster")
	age = int(input("How old are you? "))
	if age < 12:
		bill = 5
		print("Please pay $5")
	elif age <= 18:
		bill = 7
		print("Please pay $7")
	else:
		bill = 12
		print("Please pay $12")
		print("\n"*2)
		print("The cost of a photo is $12")
	wants_photo = input("Do you want a photo? y/n:  " )
	if wants_photo ==  "y":
		bill += 12
	print(f"Your total bill is ${bill}")
else:
	print("Sorry, you have to grow taller before you can ride.")

# #An improved version of the rollercoaster game

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?  "))
# bill = 0
# if height > 120:
# 	print("You can ride the rollercoaster")
# 	age = int(input("How old are you? "))
# 	if age < 12:
# 		bill = 5
# 		print("Please pay $5")
# 	elif age <= 18:
# 		bill = 7
# 		print("Please pay $7")
# 	elif age >= 45 and age <= 55:
# 		bill = 0
# 		print("You can proceed for the rollercoaster without payment")
# 	else:
# 		bill = 12
# 		print("Please pay $12")
# 		print("\n"*5)
# 		print("The cost of a photo is $12")
# 	wants_photo = input("Do you want a photo? y/n:  " )
# 	if wants_photo ==  "y":
# 		if age >= 45 and age <= 55:
# 			bill = 0
# 		else:
# 		   bill += 12
# else:
# 	print("Sorry, you have to grow taller before you can ride.")	