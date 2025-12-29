#Pizza Order Program

print("Welcome to Python Pizza Deliveries")
print("\n S = Small, \n M = Medium, \n L = Large")
size = (input("What size Pizza do you want? S, M or L:  ")).lower()
add_pepperoni = (input("Do you want to add Pepperoni? y/n:  ")).lower()
extra_cheese = (input("Do you want extra cheese? y/n:  ")).lower()

bill = 0
if size == "s":
	bill += 15
elif size == "m":
	bill += 20
else:
	bill += 25

if add_pepperoni == "y":
	if size == "s":
		bill += 2
	else:
		bill += 3

if extra_cheese == "y":
	bill += 1
print(f"Your final bill is ${bill}")



if size == "s":
	S = 15
	if add_pepperoni == "y":
		cost_p_small_p = 2
	if extra_cheese == "y":
		cost_c_small_p = 1
	
	if add_pepperoni == "n":
		cost_p_small_p = 0
	if extra_cheese == "n":
		cost_c_small_p = 0
	total = cost_c_small_p + cost_p_small_p + S
	print(f"Your final bill is ${total}")
		
	
elif size =="m"  :
	M = 20
	if add_pepperoni == "y":
		cost_p_medium_p = 3
	if extra_cheese == "y":
		cost_c_medium_p = 1
	
	if add_pepperoni == "n":
		cost_p_medium_p = 0
	if extra_cheese == "n":
		cost_c_medium_p = 0
	total = cost_c_medium_p + cost_p_medium_p + M
	print(f"Your final bill is ${total}")
elif size =="l":
	L = 25
	if add_pepperoni == "y":
		cost_p_large_p = 3
	if extra_cheese == "y":
		cost_c_large_p = 1
		
	if add_pepperoni == "n":
		cost_p_large_p = 0
	if extra_cheese == "n":
		cost_c_large_p = 0
	total = cost_c_large_p + cost_p_large_p + L
	print(f"Your final bill is ${total}")
			
else:
	print("Enter either S, M or L") \
	