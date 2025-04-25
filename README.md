# Hangman Game 🎯

Hangman is a classic word-guessing game where the player tries to uncover a hidden word by guessing one letter at a time. With each incorrect guess, a part of the hangman is drawn. The game continues until the word is guessed correctly or the figure is complete.

## Features
- Random word selection from a word list
- ASCII art for hangman stages and logo
- Tracks guessed letters
- Win and loss conditions

## Project Structure
```
hangman-game/
├── main.py              # Main game logic
├── hangman_words.py     # Contains the word list
├── hangman_art.py       # Contains ASCII art for the game
├── README.md            # Project information
└── .gitignore           # Ignored files/folders
```

## How to Run

Make sure you have Python installed.

1. Clone the repository:
```
git clone https://github.com/yourusername/hangman-game.git
cd hangman-game
```

2. Run the game:
```
python main.py
```

## Example
```
_ _ _ _ _
Guess a letter: a
Wrong! You lose a life.

_ a _ _ _
Guess a letter: e
Correct!
```

Enjoy playing Hangman! 🎉
