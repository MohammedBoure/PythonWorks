import os
import functions
import subprocess

def delete(name, filename=False):
    if filename:
        command = "del "+functions.remove_spaces(name)+".xml"
        os.system(command)
    command = 'netsh wlan delete profile name="'+name+'"'
    return os.system(command)

def connect(name):
    command = "netsh wlan connect name=\""+name+"\""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return "successfully" in result.stdout

def create(name, SSID, password, mac_address):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+password+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
    <MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
        <enableRandomization>false</enableRandomization>
    </MacRandomization>
    <MacAddress xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
        <enableRandomization>false</enableRandomization>
        <randomizationSeed>0</randomizationSeed>
        <staticMac>""" + mac_address + """</staticMac>  <!-- عنوان MAC الثابت -->
    </MacAddress>
</WLANProfile>"""

    with open(name+".xml", "w", encoding="utf-8") as file:
        file.write(config)
    
    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
    subprocess.run(command, shell=True)

create("2", "MII WII", "TyfysGWwr1", "d8:9e:61:77:ca:4f")
