# The Number Guessing Game
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty level. Type 'easy' or 'hard':  ").lower()
number = random.randint(1, 100)

# print(number)

def guess_game(guess_value, num_value):
	if guess_value > num_value:
		print("Guess to high")
	elif guess_value < num_value:
		print("Guess too low")
	else:
		print("You win") 
count = 0
end_guess = False
if level == "easy":
	guesses_remaining = 10
	while count < 10 and not end_guess:
		count += 1
		guesses_remaining -= 1
		guess = int(input("Guess a number:  "))
		guess_game(guess_value = guess, num_value = number)
		print(f"You have only {guesses_remaining} guesses remaining")
		if guess == number:
			end_guess = True
		if count == 10 and guess != number:
			print(f"You Lose. The right number is: {number}")
if level == "hard":
	guesses_remaining = 5
	while count < 5 and not end_guess:
		count += 1
		guess = int(input("Guess a number:  "))
		guess_game(guess_value = guess, num_value = number)
		print(f"You have only {guesses_remaining} guesses remaining")
		if guess == number:
			end_guess = True
		if count == 5 and guess != number:
			print(f"You Lose. The right number is: {number}")
			