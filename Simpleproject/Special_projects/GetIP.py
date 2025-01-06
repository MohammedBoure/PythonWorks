print("""Enter the last the last 16 bytes of the IP address 192.168.x.y
exp:  192.168.1.1
""")

x = input("192.168.")
y = input(f"192.168.{x}.")

for i in range(4):
    print(f"192.168.{x}.{y}")

input("press enter to exit")
