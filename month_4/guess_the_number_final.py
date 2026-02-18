from random import randint
from arts import logo
# Create a global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# Function to check user's guess against actual answer

def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS 
    

def game():
    print(logo)

    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()


    # Repeat the guessing if they get it wrong.

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(answer, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()































# # The Number Guessing Game
# import random

# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100")
# level = input("Choose a difficulty level. Type 'easy' or 'hard':  ").lower()
# number = random.randint(1, 100)

# # print(number)

# def guess_game(guess_value, num_value):
# 	if guess_value > num_value:
# 		print("Guess to high")
# 	elif guess_value < num_value:
# 		print("Guess too low")
# 	else:
# 		print("You win") 
# count = 0
# end_guess = False
# if level == "easy":
# 	guesses_remaining = 10
# 	while count < 10 and not end_guess:
# 		count += 1
# 		guesses_remaining -= 1
# 		guess = int(input("Guess a number:  "))
# 		guess_game(guess_value = guess, num_value = number)
# 		print(f"You have only {guesses_remaining} guesses remaining")
# 		if guess == number:
# 			end_guess = True
# 		if count == 10 and guess != number:
# 			print(f"You Lose. The right number is: {number}")
# if level == "hard":
# 	guesses_remaining = 5
# 	while count < 5 and not end_guess:
# 		count += 1
# 		guess = int(input("Guess a number:  "))
# 		guess_game(guess_value = guess, num_value = number)
# 		print(f"You have only {guesses_remaining} guesses remaining")
# 		if guess == number:
# 			end_guess = True
# 		if count == 5 and guess != number:
# 			print(f"You Lose. The right number is: {number}")
			