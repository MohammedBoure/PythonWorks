from scapy.all import *



#option
def analyzer(pkt):
    #if pkt.haslayer(UDP):
    print(pkt)
print("**************STARTED***************")
# Sniff packets on the "Wi-Fi" interface and call the analyzer function for each packet
sniff(iface="Wi-Fi", prn=analyzer)
