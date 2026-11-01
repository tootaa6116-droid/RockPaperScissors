
import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

# Main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x480")
window.resizable(False, False)

# Title
title = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 24, "bold")
)
title.pack(pady=25)

instructions = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 14)
)
instructions.pack(pady=10)

# Result
result_label = tk.Label(
    window,
    text="Make your choice!",
    font=("Arial", 14)
)
result_label.pack(pady=20)

# Score
score_label = tk.Label(
    window,
    text="Player: 0 | Computer: 0",
    font=("Arial", 14, "bold")
)
score_label.pack(pady=10)


# Play function
def play(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "Draw!"

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(
        text=f"You: {player_choice} | Computer: {computer_choice}\n{result}"
    )

    update_score()


# Update score function
def update_score():
    score_label.config(
        text=f"Player: {player_score} | Computer: {computer_score}"
    )


# Reset function
def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    result_label.config(text="New Game! Make your choice!")
    update_score()


# Choice buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack(pady=20)

for choice in choices:
    button = tk.Button(
        buttons_frame,
        text=choice,
        width=10,
        font=("Arial", 12),
        command=lambda c=choice: play(c)
    )
    button.pack(side=tk.LEFT, padx=5)

# Reset button
reset_button = tk.Button(
    window,
    text="Reset Game",
    width=15,
    font=("Arial", 12, "bold"),
    command=reset_game
)
reset_button.pack(pady=20)

window.mainloop()
