import tkinter as tk
import FunctionForTkinter








# Create the main window
scap = tk.Tk()
scap.title("Scap")
scap.configure(bg="#303841")  # Set the background color of the main window
#scap.geometry("300x200")  # Set the size of the window (width x height)

button = tk.Button(scap, text="ICMP", command=FunctionForTkinter.icmp_inter, bg="lightgreen", fg="black", width=10, height=3)
button.pack(pady=10,padx=10, ipadx=100, ipady=5)

button = tk.Button(scap, text="sniff pkt", command=FunctionForTkinter.sniff_pkt_inter, bg="lightgreen", fg="black", width=10, height=3)
button.pack(pady=10,padx=10, ipadx=100, ipady=5)

scap.mainloop()







frame1 = tk.Frame(scap, bg="black")
frame1.grid(row=0, column=0, padx=10, pady=10, ipadx=5, ipady=5, rowspan=2, columnspan=1, sticky="nsew")

label = tk.Label(frame1, text="Enter your name:", bg="lightblue", fg="black")
label.pack(expand=True, fill="both")

frame2 = tk.Frame(scap, bg="lightyellow")
frame2.grid(row=0, column=1, padx=10, pady=10, ipadx=5, ipady=5, rowspan=1, columnspan=2, sticky="nsew")

entry = tk.Entry(frame2, bg="white", fg="black")
entry.pack(expand=True, fill="both")

frame3 = tk.Frame(scap, bg="lightgreen")
frame3.grid(row=1, column=1, padx=10, pady=10, ipadx=5, ipady=5, rowspan=1, columnspan=2, sticky="nsew")

button = tk.Button(frame3, text="Greet", command=on_button_click, bg="lightgreen", fg="black")
button.pack(expand=True, fill="both")

root.mainloop()





global text_widget
text_widget = tk.Text(icmp_inte, height=10, width=50, bg="black", fg="lightgreen", font=("Arial", 10))
text_widget.pack(pady=10, padx=10)
text_widget.config(state=tk.DISABLED)  # Make the Text widget read-only initially
