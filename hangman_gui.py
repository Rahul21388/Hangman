import tkinter as tk
import random
from hangman_words import word_list
from hangman_art import stages

# Initialize game state
chosen_word = random.choice(word_list)
word_display = ["_" for _ in chosen_word]
guessed_letters = []
lives = 6

# Functions
def update_display():
    word_label.config(text=" ".join(word_display))
    guesses_label.config(text=f"Guessed Letters: {', '.join(guessed_letters)}")
    lives_label.config(text=f"Lives Left: {lives}")
    stage_label.config(text=stages[6 - lives])
    if "_" not in word_display:
        result_label.config(text="🎉 You win!")
        guess_entry.config(state="disabled")
    elif lives <= 0:
        result_label.config(text=f"💀 You lose! Word was: {chosen_word}")
        guess_entry.config(state="disabled")

def submit_guess():
    global lives
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if not guess.isalpha() or len(guess) != 1:
        result_label.config(text="Enter one alphabet letter.")
        return
    if guess in guessed_letters:
        result_label.config(text=f"You already guessed '{guess}'.")
        return

    guessed_letters.append(guess)
    if guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[idx] = guess
        result_label.config(text=f"✅ Correct: {guess}")
    else:
        lives -= 1
        result_label.config(text=f"❌ Wrong: {guess}")

    update_display()

# UI Setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x500")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="🎯 Hangman Game", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

word_label = tk.Label(root, text=" ".join(word_display), font=("Courier", 24), bg="#f0f0f0")
word_label.pack(pady=10)

lives_label = tk.Label(root, text=f"Lives Left: {lives}", font=("Helvetica", 14), bg="#f0f0f0")
lives_label.pack()

guesses_label = tk.Label(root, text="Guessed Letters: ", font=("Helvetica", 12), bg="#f0f0f0")
guesses_label.pack(pady=5)

stage_label = tk.Label(root, text=stages[0], font=("Courier", 12), bg="#f0f0f0")
stage_label.pack(pady=5)

guess_entry = tk.Entry(root, font=("Helvetica", 14), width=5, justify="center")
guess_entry.pack(pady=10)

submit_button = tk.Button(root, text="Guess", font=("Helvetica", 12), command=submit_guess)
submit_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

update_display()
root.mainloop()
