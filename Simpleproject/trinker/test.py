import tkinter as tk

def on_button_click():
    print(f"Hello, {entry.get()}!")

root = tk.Tk()
root.title("Tkinter Grid Example")
root.configure(bg="#303841")


frame1 = tk.Frame(root, bg="black")
frame1.grid(row=0, column=0, padx=10, pady=10, ipadx=5, ipady=5, rowspan=2, columnspan=1, sticky="nsew")

label = tk.Label(frame1, text="Enter your name:", bg="lightblue", fg="black")
label.pack(expand=True, fill="both")

frame2 = tk.Frame(root, bg="lightyellow")
frame2.grid(row=0, column=1, padx=10, pady=10, ipadx=5, ipady=5, rowspan=1, columnspan=2, sticky="nsew")

entry = tk.Entry(frame2, bg="white", fg="black")
entry.pack(expand=True, fill="both")

frame3 = tk.Frame(root, bg="lightgreen")
frame3.grid(row=1, column=1, padx=10, pady=10, ipadx=5, ipady=5, rowspan=1, columnspan=2, sticky="nsew")

button = tk.Button(frame3, text="Greet", command=on_button_click, bg="lightgreen", fg="black")
button.pack(expand=True, fill="both")

root.mainloop()
