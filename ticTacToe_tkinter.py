import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x450")
root.configure(bg="lightblue")

# Global variables
board = [[None for _ in range(3)] for _ in range(3)]
player_turn = "O"

# Update the turn prompt
def update_prompt():
    turn_label["text"] = f"Player {player_turn}'s Turn"

def button_click(row, col):
    global player_turn
    if board[row][col]["text"] == "":
        board[row][col]["text"] = player_turn
        board[row][col]["state"] = "disabled"  # Disable the button after it's clicked
        winner = check_winner()
        if winner:
            result_label["text"] = f"Player {player_turn} Wins!"
            highlight_winner()
            disable_buttons()
        elif all_buttons_filled():
            result_label["text"] = "It's a Draw!"
        else:
            player_turn = "X" if player_turn == "O" else "O"
            update_prompt()

# Check for a winner
def check_winner():
    for i in range(3):
        # Check rows
        if board[i][0]["text"] == board[i][1]["text"] == board[i][2]["text"] != "":
            return [(i, 0), (i, 1), (i, 2)]
        # Check columns
        if board[0][i]["text"] == board[1][i]["text"] == board[2][i]["text"] != "":
            return [(0, i), (1, i), (2, i)]
    # Check diagonals
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        return [(0, 0), (1, 1), (2, 2)]
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        return [(0, 2), (1, 1), (2, 0)]
    return None


# Highlight the winning row, column, or diagonal
def highlight_winner():
    winner = check_winner()
    if winner:
        for (row, col) in winner:
            board[row][col].config(bg="lightgreen")

# Check if all buttons are filled
def all_buttons_filled():
    for i in range(3):
        for j in range(3):
            if board[i][j]["text"] == "":
                return False
    return True

# Disable all buttons
def disable_buttons():
    for i in range(3):
        for j in range(3):
            board[i][j]["state"] = "disabled"

# Reset the game
def reset_game():
    global player_turn
    player_turn = "O"
    result_label["text"] = ""
    update_prompt()
    for i in range(3):
        for j in range(3):
            board[i][j]["text"] = ""
            board[i][j]["state"] = "normal"
            board[i][j].config(bg="white")

# Title
title_label = tk.Label(root, text="Tic Tac Toe", font=("Helvetica", 24, "bold"), bg="lightblue", fg="darkblue")
title_label.pack(pady=10)

# Turn prompt
turn_label = tk.Label(root, text=f"Player {player_turn}'s Turn", font=("Helvetica", 18), bg="lightblue")
turn_label.pack()

# Create the game board
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=20)
for i in range(3):
    for j in range(3):
        button = tk.Button(frame, text="", font=("Helvetica", 20), width=5, height=2, 
                           bg="white", command=lambda row=i, col=j: button_click(row, col))
        button.grid(row=i, column=j, padx=5, pady=5)
        board[i][j] = button

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="lightblue", fg="red")
result_label.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), command=reset_game, bg="white", fg="black")
reset_button.pack(pady=10)

# Start the game loop
update_prompt()
root.mainloop()
