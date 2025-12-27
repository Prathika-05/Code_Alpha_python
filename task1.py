import random

# Predefined list of words
words = ["python", "hangman", "coding", "random", "string"]

# Choose a random word
secret_word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Create display word with underscores
display_word = ["_"] * len(secret_word)

print("Welcome to Hangman!")
print("You have 6 incorrect guesses.\n")

# Game loop
while incorrect_guesses < max_incorrect and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")

    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in secret_word:
        print("Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!\n")
        incorrect_guesses += 1

# End of game
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game Over! The word was:", secret_word)
