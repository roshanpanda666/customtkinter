import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("400x450")
root.title("Tic-Tac-Toe with CustomTkinter")

current_player = "X"
board = [""] * 9
buttons = []

def check_winner():
    win_combos = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]
    for combo in win_combos:
        a,b,c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def handle_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].configure(text=current_player)
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Result", "It's a draw!")
            else:
                messagebox.showinfo("Result", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.configure(text=f"Player {current_player}'s turn")

def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.configure(text="", state="normal")
    status_label.configure(text="Player X's turn")

frame = ctk.CTkFrame(root)
frame.pack(pady=20)

for i in range(9):
    btn = ctk.CTkButton(frame, text="", font=("Arial", 30), width=80, height=80,
                        command=lambda i=i: handle_click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

status_label = ctk.CTkLabel(root, text="Player X's turn", font=("Arial", 18))
status_label.pack(pady=10)

reset_btn = ctk.CTkButton(root, text="Restart", command=reset_game)
reset_btn.pack()

root.mainloop()
