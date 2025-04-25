import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game setup
display = ["_" for _ in range(word_length)]
lives = 6
guessed_letters = []

# Main game loop
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        print(f"Correct! {guess} is in the word.")
    else:
        lives -= 1
        print(f"Wrong! You lost a life. Lives left: {lives}")
        print(stages[6 - lives])

    print("Word: " + " ".join(display))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("-" * 40)

# End of game
if "_" not in display:
    print("🎉 You win! The word was:", chosen_word)
else:
    print("💀 You lose. The word was:", chosen_word)
