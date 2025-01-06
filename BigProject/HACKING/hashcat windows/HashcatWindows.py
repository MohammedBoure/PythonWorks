import os

path_hashcat = input("enter hashcat path: ")
mode_prossece = input("enter mode prossece GPU or CPU:")
num_hs = int(input("enter number files hash:"))
num_wl = int(input("enter number files wordliste:"))

os.chdir(path_hashcat)

hs,wl = 1,1
if mode_prossece == "CPU":
    while hs<=num_hs:
        while wl<=num_wl:
            os.system("hashcat -D 1 -m 22000 -a 0 a/"+str(hs)+".txt a/wl"+str(wl)+".txt")
            wl += 1
        hs += 1
if mode_prossece == "GPU":
    while hs<=num_hs:
        while wl<=num_wl:
            os.system("hashcat -m 22000 -a 0 a/"+str(hs)+".txt a/wl"+str(wl)+".txt")
            wl += 1
        hs += 1


