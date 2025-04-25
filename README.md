# Hangman Game 🎯

**Hangman** is a simple and fun word-guessing game written in Python. The player tries to guess a hidden word one letter at a time. For every incorrect guess, a part of the hangman is drawn. The game ends when the player either guesses the word or the hangman is fully drawn.

## Features
- Random word selection from a predefined list
- ASCII art visuals for each stage of the game
- Clear tracking of guessed letters
- Win/Lose end conditions

## Project Structure
```
hangman-game/
├── main.py              # Main game logic
├── hangman_words.py     # Contains the word list
├── hangman_art.py       # Contains ASCII art for the game
├── README.md            # Project information
└── .gitignore           # Ignored files/folders
```

## Sample Gameplay
```
_ _ _ _ _
Guess a letter: a
Wrong! You lose a life.

_ a _ _ _
Guess a letter: e
Correct!
```

Enjoy the game, and feel free to customize the word list or ASCII art! 🎉
