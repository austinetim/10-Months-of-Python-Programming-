# This program is built ti mimick the popular hangman game

# Step 1
import random
import hangman_words
import hangman_arts

print(hangman_arts.logo)


word_list = hangman_words.word_list 


# Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"


# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to 6

lives = 6

end_of_game = False
while not end_of_game:
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    # print(f"{" ".join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Print the ascii are from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    print(hangman_arts.stages[lives])



