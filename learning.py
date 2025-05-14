import customtkinter as ctk

ctk.set_appearance_mode("System")  # Light, Dark, or System
ctk.set_default_color_theme("blue")  # Themes: blue, green, dark-blue

root = ctk.CTk()  # Use CTk instead of Tk
root.geometry("400x300")
root.title("CustomTkinter Window")

def clickmefun():
    var1=0
    for var1 in range(100):
        print("hello world",var1)
        var1=var1+1

button1 = ctk.CTkButton(root, text="click", command=(clickmefun))
button1.pack(pady=20)

root.mainloop()
