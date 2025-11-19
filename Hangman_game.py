import random

# Predefined list of 5 words
words = ["python", "hangman", "coding", "simple", "games"]

# Choose a random word
secret_word = random.choice(words)

# Create a list to store guessed letters
guessed_word = ["_"] * len(secret_word)

# Set of guessed letters
guessed_letters = set()

# Maximum incorrect guesses
max_attempts = 6
incorrect_attempts = 0

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("Word:", " ".join(guessed_word))

while incorrect_attempts < max_attempts and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    # Validate input (must be a single alphabet)
    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter only one alphabet letter.")
        continue

    # Prevent repeated guesses
    if guess in guessed_letters:
        print(" You already guessed that letter!")
        continue
    
    guessed_letters.add(guess)

    # Check if guess is correct
    if guess in secret_word:
        print(" Correct guess!")

        # Reveal letters in the guessed_word list
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        incorrect_attempts += 1
        print(f" Wrong guess! Attempts left: {max_attempts - incorrect_attempts}")

    print("Word:", " ".join(guessed_word))

# Game result
if "_" not in guessed_word:
    print("\n Congratulations! You guessed the word:", secret_word)
else:
    print("\n Game Over! The correct word was:", secret_word)
