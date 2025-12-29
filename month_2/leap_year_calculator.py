#LEAP YEAR CALCULATOR

#Covert the string input into an integer
year = int(input("Enter a year:  "))

# Using if-else statement and logical operators
if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
	print(f"{year} is a Leap Year")
else:
	print(f"{year} is not a Leap year")

# # Using if-else statement and modulus	
# if year % 4 == 0:
# 	if year % 100 != 0:
# 		if year % 400 != 0:
# 			print(f"{year} is a Leap year")
# 	else:
# 		print(f"{year} is a Leap year")
# else:
# 	print(f"{year} is not  Leap year")
