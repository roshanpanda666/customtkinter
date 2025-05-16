import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("400x600")
root.title("To-Do List 📝")

# Global task list
tasks = []

# Frame for entire app
main_frame = ctk.CTkFrame(master=root)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Heading
heading = ctk.CTkLabel(main_frame, text="To-Do List 🧠", font=("Arial", 24))
heading.pack(pady=10)

# Entry field for new task
task_input = ctk.CTkEntry(main_frame, placeholder_text="Enter a new task...")
task_input.pack(pady=10, fill="x", padx=10)

# Frame to hold all tasks
task_frame = ctk.CTkScrollableFrame(main_frame, width=360, height=400)
task_frame.pack(pady=10)

# Function to add task
def add_task():
    task_text = task_input.get().strip()
    if task_text == "":
        return

    task_row = ctk.CTkFrame(master=task_frame)
    task_row.pack(pady=5, fill="x", padx=5)

    task_label = ctk.CTkLabel(master=task_row, text=task_text, anchor="w")
    task_label.pack(side="left", fill="x", expand=True, padx=10)

    def mark_done():
        task_label.configure(text=f"✔️ {task_label.cget('text')}", text_color="green")

    def delete_task():
        task_row.destroy()

    done_button = ctk.CTkButton(task_row, text="✓", width=30, command=mark_done)
    done_button.pack(side="right", padx=2)

    delete_button = ctk.CTkButton(task_row, text="🗑", width=30, fg_color="red", hover_color="darkred", command=delete_task)
    delete_button.pack(side="right", padx=2)

    task_input.delete(0, 'end')

# Add button
add_btn = ctk.CTkButton(main_frame, text="Add Task", command=add_task)
add_btn.pack(pady=10)

root.mainloop()
