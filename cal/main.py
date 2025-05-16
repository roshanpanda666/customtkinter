import customtkinter as ctk
from sound import click
from sound import resultsound
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("350x500")
root.title("Custom Calculator")

# Frame
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Display label
display_text = ctk.StringVar(value="")
display = ctk.CTkLabel(master=frame, textvariable=display_text, font=("Arial", 24), text_color="white")
display.pack(pady=10)

# Logic variables
first_argument = ""
operation = ""
second_argument = ""
step = 1  # To track what we're filling: 1st arg, operator, or 2nd arg

# Button click handler
def button_click(value):
    click()
    global first_argument, operation, second_argument, step

    if step == 1:
        first_argument += value
        display_text.set(first_argument)
    elif step == 2:
        operation = value
        display_text.set(first_argument + " " + operation)
        step = 3
    elif step == 3:
        second_argument += value
        display_text.set(first_argument + " " + operation + " " + second_argument)

# Equals (=) button logic
def calculate_result():
    
    global first_argument, operation, second_argument, step
    try:
        if operation == "+":
            result = int(first_argument) + int(second_argument)
        elif operation == "-":
            result = int(first_argument) - int(second_argument)
        elif operation == "*":
            result = int(first_argument) * int(second_argument)
        elif operation == "/":
            result = int(first_argument) / int(second_argument)
        else:
            result = "Invalid op"

        display_text.set(str(result))
        resultsound()
    except Exception as e:
        display_text.set("Error")

    # Reset for next calculation
    first_argument = ""
    operation = ""
    second_argument = ""
    step = 1

# Create button grid
buttons_frame = ctk.CTkFrame(master=frame)
buttons_frame.pack(pady=10)

# Buttons layout
button_values = [
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '*'],
    ['0', '=', 'C', '/']
]

for row in button_values:
    row_frame = ctk.CTkFrame(master=buttons_frame)
    row_frame.pack(side="top", pady=5)
    for val in row:
        if val == '=':
            btn = ctk.CTkButton(master=row_frame, text=val, width=60, command=calculate_result)
        elif val == 'C':
            btn = ctk.CTkButton(master=row_frame, text=val, width=60, command=lambda: clear_all())
        else:
            btn = ctk.CTkButton(master=row_frame, text=val, width=60, command=lambda v=val: handle_input(v))
        btn.pack(side="left", padx=5)

# Handle input and step logic
def handle_input(value):
    global step
    if step == 1:
        if value.isdigit():
            button_click(value)
        else:
            step = 2
            button_click(value)
    elif step == 2:
        button_click(value)
    elif step == 3:
        button_click(value)

# Clear all
def clear_all():
    global first_argument, second_argument, operation, step
    first_argument = ""
    second_argument = ""
    operation = ""
    step = 1
    display_text.set("")

root.mainloop()
