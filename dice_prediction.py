import tkinter as tk
import random

root = tk.Tk()
root.title("Dice Prediction Game")
root.geometry("600x650")
root.configure(bg="#F8C8DC")

prediction = tk.StringVar()
prediction.set("5")

# Score starts at zero
score = 0

title = tk.Label(
    root,
    text="🎲 DICE PREDICTION",
    font=("Arial", 24, "bold"),
    bg="#F8C8DC",
    fg="#702747"
)
title.pack(pady=(45, 10))

subtitle = tk.Label(
    root,
    text="Pick a number. Test your luck.",
    font=("Arial", 13),
    bg="#F8C8DC",
    fg="#702747"
)
subtitle.pack(pady=5)

choice = tk.OptionMenu(
    root, prediction, "1", "2", "3", "4", "5", "6"
)
choice.config(
    font=("Arial", 12),
    bg="#FFF0F5",
    fg="#702747",
    width=15
)
choice.pack(pady=25)

# Display the current score
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 16, "bold"),
    bg="#F8C8DC",
    fg="#702747"
)
score_label.pack(pady=10)

def roll_dice():
    global score

    guess = int(prediction.get())
    dice = random.randint(1, 6)

    if guess == dice:
        score = score + 1
        result.config(text=f"You won! Dice: {dice}")
    else:
        result.config(text=f"Try again! Dice: {dice}")

    # Update the score after every roll
    score_label.config(text=f"Score: {score}")

button = tk.Button(
    root,
    text="ROLL DICE",
    command=roll_dice,
    bg="#D96C93",
    fg="white",
    font=("Arial", 14, "bold"),
    width=18,
    relief="flat",
    cursor="hand2"
)
button.pack(pady=20)

result = tk.Label(
    root,
    text="Your prediction goes here",
    font=("Arial", 13),
    bg="#FCE4EC",
    fg="#702747",
    width=30,
    height=3,
    relief="solid",
    bd=1
)
result.pack(pady=15)

footer = tk.Label(
    root,
    text="— GOOD LUCK! —",
    font=("Arial", 12, "bold"),
    bg="#F8C8DC",
    fg="#702747"
)
footer.pack(pady=20)

root.mainloop()