# Hangman Game 🎯

**Hangman** is a classic word-guessing game implemented in Python with both command-line and graphical user interface (GUI) versions. The player tries to guess a randomly chosen word, one letter at a time. For every incorrect guess, a part of the hangman is drawn. The game ends when the player either guesses the word correctly or loses all lives.

---

## 🔧 Features
- Random word selection from a word list
- ASCII art visual stages for incorrect guesses
- GUI version using Tkinter
- Tracks guessed letters and lives
- Win and loss conditions

---

## 📁 Project Structure

```
hangman-game/
├── main.py                # CLI-based Hangman game
├── hangman_gui.py         # GUI version using Tkinter
├── hangman_words.py       # List of possible words
├── hangman_art.py         # ASCII art stages and logo
├── Hangman Flowchart.jpg  # Project Flowchart
└── README.md              # Project overview and instructions
```

---

## ▶️ How to Run

### 🖥️ Run Command-Line Version

Make sure Python is installed.

```bash
python main.py
```

### 🪟 Run GUI Version (Tkinter)

```bash
python hangman_gui.py
```

> No external packages are required. Tkinter comes built-in with standard Python distributions.

---

## 🕹️ Sample Gameplay (CLI)

```
_ _ _ _ _
Guess a letter: a
Wrong! You lose a life.

_ a _ _ _
Guess a letter: e
Correct!
```

---

Enjoy playing Hangman — now in both terminal and GUI style! 🎉  
Feel free to fork and enhance with word categories, themes, or difficulty settings.
