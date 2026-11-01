
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x450")
window.resizable(False, False)

# Title
title = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 24, "bold")
)
title.pack(pady=25)

# Instructions
instructions = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 14)
)
instructions.pack(pady=10)

# Choice buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack(pady=20)

rock_button = tk.Button(
    buttons_frame, text="Rock", width=10, font=("Arial", 12)
)
rock_button.pack(side=tk.LEFT, padx=5)

paper_button = tk.Button(
    buttons_frame, text="Paper", width=10, font=("Arial", 12)
)
paper_button.pack(side=tk.LEFT, padx=5)

scissors_button = tk.Button(
    buttons_frame, text="Scissors", width=10, font=("Arial", 12)
)
scissors_button.pack(side=tk.LEFT, padx=5)

# Result
result_label = tk.Label(
    window,
    text="Your result will appear here",
    font=("Arial", 14)
)
result_label.pack(pady=25)

# Score
score_label = tk.Label(
    window,
    text="Player: 0 | Computer: 0",
    font=("Arial", 14, "bold")
)
score_label.pack(pady=10)

# Start the application
window.mainloop()
