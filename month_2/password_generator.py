# password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['@', '#', '$', '%', '&', '*', '(', ')', '!', '?', "+"]

print("Welcome to the Password Generator")

nr_letters = int(input("How many letters would like in your password?\n"))
nr_symbols = int(input("How many symbols would like?\n"))
nr_numbers = int(input("How many numbers would like?\n"))
nr_total = nr_letters + nr_symbols + nr_numbers
print(f"Total number of characters in password: {nr_total}")

# Using random.sample()
# Here the password is created without repeated charaters

selected_letters = random.sample(letters, nr_letters)
selected_numbers = random.sample(numbers, nr_numbers)
selected_symbols = random.sample(symbols, nr_symbols)

#print(selected_letters)
#print(selected_numbers)
#print(selected_symbols)

gen_pass = selected_letters + selected_numbers + selected_symbols

# Re-randomize the list to get a random mixture of letters, symbols and numbers
gen_pass = random.sample(gen_pass, len(gen_pass))
print(gen_pass)
#Join the characters together and store in a variable
final_pass = "".join(gen_pass)
print(f"Here is your final password: {final_pass}")


# # Using random.choices()
# # Here the password is created with or without repeated characters

# selected_letters = random.choices(letters, k=nr_letters)
# selected_numbers = random.choices(numbers, k=nr_numbers)
# selected_symbols = random.choices(symbols, k=nr_symbols)
# print(type(selected_letters[0]))

# print(selected_letters)
# print(selected_numbers)
# print(selected_symbols)

# gen_pass = selected_letters + selected_numbers + selected_symbols
# print(gen_pass)
 
# # Re-randomize the list to get a random mixture of letters, symbols and numbers
# gen_pass = random.sample(gen_pass, len(gen_pass))

# # Join the charaters together and store in a variable

# final_pass = ''.join(gen_pass)
# print(f"Here is your password: {final_pass}")