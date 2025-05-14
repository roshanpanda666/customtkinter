import customtkinter as ctk
from loop import print_hello_world
from sound import play

ctk.set_appearance_mode("system")  # Light, Dark, or System
ctk.set_default_color_theme("blue")  # Themes: blue, green, dark-blue

root = ctk.CTk()  # Use CTk instead of Tk
root.geometry("400x300")
root.title("CustomTkinter Window")

def clickmefun():
        print_hello_world()

def playsoundfun():
        play()

button1 = ctk.CTkButton(root, text="click", command=(clickmefun))
button1.pack(pady=20,side="left",padx="20")

button2=ctk.CTkButton(root,text="playsound",command=(playsoundfun))
button2.pack(pady=20,side="right",padx="20")

root.mainloop()