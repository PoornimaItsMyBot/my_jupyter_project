

import random
import hangman_words

# ASCII art for different stages of the hangman
hangman_stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    '''
]

# Randomly choose a word from the word list
ran_word = random.choice(hangman_words.list_words)

lives = 6
print(ran_word)  # This line can be removed if you don't want to reveal the word
placeholder = "-" * len(ran_word)
print(placeholder)

game_over = False
correct_letters = []  # List of correctly guessed letters
incorrect_letters = []  # List of incorrectly guessed letters

while not game_over:
    letter = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if letter in correct_letters or letter in incorrect_letters:
        print(f"You already guessed '{letter}'. Try a different letter.")
        continue  # Skip the rest of the loop to avoid processing this letter again

    # Update the display if the letter is in the word
    display = ""
    if letter in ran_word:
        correct_letters.append(letter)  # Track correct guesses
        for i in ran_word:
            if i in correct_letters:
                display += i
            else:
                display += "-"
    else:
        incorrect_letters.append(letter)  # Track incorrect guesses
        lives -= 1
        print(hangman_stages[6 - lives])  # Display the hangman stage corresponding to the number of lives left
        print(f"Incorrect guess. Lives left: {lives}")
        if lives == 0:
            game_over = True
            print(f"You lose! The correct word was '{ran_word}'.")
            break  # Exit the loop after showing the correct word

    # Show the updated word display
    print(display)

    # Check if the player has won
    if "-" not in display:
        game_over = True
        print("Congratulations, you win!")
