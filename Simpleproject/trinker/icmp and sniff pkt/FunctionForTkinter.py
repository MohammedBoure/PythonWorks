import FunctionNT
import tkinter as tk



##this part for icmp
def icmp_inter():
    def icmp_fnc(ip, count):
        try:
            # Convert count to integer
            count = int(count)
            # Create an instance of the Scapy class and call the icmp method
            cs = FunctionNT.Scapy()
            cs.icmp(ip, count)
            print(f"ICMP packets sent to {ip} with count {count}")
        except ValueError:
            print("Invalid count value. Please enter a number.")

    # Create a new Tkinter window for ICMP attack
    icmp_inte = tk.Tk()
    icmp_inte.title("ICMP Attack")
    icmp_inte.configure(bg="#303841")


    # Add a label and entry widget to the new window
    label = tk.Label(icmp_inte, text="Enter target IP:", bg="#303841", fg="lightgreen")
    label.pack(pady=10)

    entry1 = tk.Entry(icmp_inte, fg="lightgreen", bg="black", font=("Arial", 10), justify="center")
    entry1.pack(pady=10, ipadx=50, ipady=4)

    label = tk.Label(icmp_inte, text="Enter count:", bg="#303841", fg="lightgreen")
    label.pack(pady=10)

    entry2 = tk.Entry(icmp_inte, fg="lightgreen", bg="black", font=("Arial", 10), justify="center")
    entry2.pack(pady=10, ipadx=50, ipady=4)

    # Button to trigger ICMP action
    attack_button = tk.Button(icmp_inte, text="Send ICMP", command=lambda: icmp_fnc(entry1.get(),entry2.get()), bg="lightgreen", fg="black")
    attack_button.pack(pady=10)

    icmp_inte.mainloop()




def sniff_pkt_inter():

    sniff_inte = tk.Tk()
    sniff_inte.title("sniff pkt")
    sniff_inte.configure(bg="#303841")

    text = """
    You can use the following filters:
             filter="icmp"  # Capture only ICMP packets
             filter="tcp"   # Capture only TCP packets
             filter="udp"   # Capture only UDP packets
             filter="tcp port 80"  # Capture TCP packets on port 80 (HTTP)
             filter="host 192.168.1.1"  # Capture packets from/to a specific IP address              
             ....
             ...
"""
    label = tk.Label(sniff_inte, text=text, bg="#303841", fg="lightgreen", justify="center")
    label.pack(expand=True, fill="both")

    filter_var = tk.StringVar(sniff_inte)
    filter_var.set("Select a filter")
    filters = ["icmp", "tcp", "udp", "tcp port ******","udp port ******", "host ***.***.***.***"]
    filter_menu = tk.OptionMenu(sniff_inte, filter_var, *filters)
    filter_menu.pack(pady=5, ipadx=20, ipady=4)

    entry = tk.Entry(sniff_inte, fg="lightgreen", bg="black", font=("Arial", 10), justify="center")
    entry.pack(pady=10, ipadx=50, ipady=4)

    cs = FunctionNT.Scapy()
    button = tk.Button(sniff_inte, text="start sniff", command=lambda: cs.sniff_pkt(filter_var.get() + " " + entry.get()), bg="lightgreen", fg="black")
    button.pack(pady=10)



