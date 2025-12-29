
#LOVE SCORE CALCULATOR
#used functions: lower(), count()---counts the number of string occurrence

print("Welcome To The Love Calculator")
name1 = (input("What is your name?  \n")).lower()
print(type(name1))
name2 = (input("What is their name?  \n")).lower()

print(name1+ " " +name2)
#word1 = "true"
#word2 = "love"
alph_check1= name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
alph_check2= name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
score = int(str(alph_check1) + str(alph_check2))
if (score < 10) or (score > 90):
	print(f"Your score is {score}, you go together like coke and mentos")
elif (score >= 40) and (score <= 50):
	print(f"Your score is {score}, you are alright together")
else:
	print(f"Your score is {score}")
	
# #Improved version of the lovescore calculator

# print("Welcome To The Love Calculator")
# name1 = input("What is your name?  \n")
# print(type(name1))
# name2 = input("What is their name?  \n")

# name_case = (name1 + name2).lower()
# print(name_case)

# t = name_case.count("t")
# r = name_case.count("r")
# u = name_case.count("u")
# e = name_case.count("e")

# true = t + r + u + e
# print(true)

# l = name_case.count("l")
# o = name_case.count("o")
# v = name_case.count("v")
# e = name_case.count("e")

# love = l + o + v + e
# print(love)

# score = int(str(true) + str(love))

# if (score < 10) or (score > 90):
# 	print(f"Your score is {score}, you go together like coke and mentos")
# elif (score >= 40) and (score <= 50):
# 	print(f"Your love score is {score}, you are alright together")
# else:
# 	print(f"Your score is {score}")