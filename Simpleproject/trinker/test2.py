import tkinter as tk
from tkinter import ttk

def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Custom Title Bar Example")
root.geometry("300x200")
root.configure(bg="#2E2E2E")

root.overrideredirect(True)

title_bar = tk.Frame(root, bg="#1E1E1E", relief="raised", bd=2, height=30)
title_bar.pack(fill="x")

button = tk.Button(title_bar, text="name", command=print(1), bg="black", fg="white", font=("Arial",8), relief="flat")
button.pack(side="left", padx=5)

close_button = tk.Button(title_bar, text="X", command=close_window, bg="black", fg="white", font=("Arial",8), relief="flat")
close_button.pack(side="right", padx=5)

title_bar.bind("<B1-Motion>", move_window)

content_frame = tk.Frame(root, bg="#3E3E3E")
content_frame.pack(fill="both", expand=True, padx=10, pady=10)

label = tk.Label(content_frame, text="Hello, World!", bg="#3E3E3E", fg="white")
label.pack(pady=20)

root.mainloop()
