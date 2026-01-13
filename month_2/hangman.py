# This program is built ti mimick the popular hangman game

# Step 1
import random
word_list = ["advark", "baboon", "camel"]

#todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

# TO_DO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# TO_DO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")

#     else:
#         print("Wrong")

# 13/01/2026

# TO_DO-2: - Loop through each position in the chosen_word;
#If the letter at the position matches 'guess' then reveal that letter in the display at that position. 

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TO_DO 3 - Use a while loop to let the user guess again. The loop should only stop once the user guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# My Code
# guess_checker = ["a"]   
# while len(guess_checker) < len(chosen_word):
#     guess = input("Guess a letter: ").lower()
#     guess_checker += guess
#     for letter in range(0, len(chosen_word)):
#         if guess == chosen_word[letter]:
#             display += guess
#         else:
#             display += "_"

# display = " ".join(display)
# print(display)
end_of_game = False
while not end_of_game:
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
