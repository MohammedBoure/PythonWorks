import tkinter as tk

def on_button_click():
    print(entry.get())

root = tk.Tk()
root.title("Tkinter Example")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet", command=on_button_click)
button.pack()

root.mainloop()
