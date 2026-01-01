import random
test_seed = int(input("Create seed number:  "))
random.seed(test_seed)

# Split the string

namesAsCsv = input("Give me everybody's name separated by comma:  ")
names = namesAsCsv.split(", ")

# Get the length of the list of values
length = len(names)

# Randomize who to pay the bill using the index values
random_pay = random.randint(0, length-1)
person_will_pay = names[random_pay]
who_to_pay = f"{person_will_pay} is going to buy the meal today!"
print(who_to_pay)