# This program is built to mimick the popular hangman game


import random
import hangman_words
import hangman_arts
from clear_terminal import clear

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
    
    guess = input("Guess a letter: ").lower()
    #Clear the screen
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{" ".join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_arts.stages[lives])



