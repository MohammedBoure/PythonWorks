from scapy.all import *


class Scapy:
    
    def icmp(self, target_ip, count):
        # Build an ICMP packet
        packet = IP(dst=target_ip)/ICMP()

        # Function to send ICMP packets repeatedly
        for _ in range(count):
            send(packet)  # Send ICMP packets repeatedly


    def sniff_pkt(self,filter_):
        def analyzer(pkt):
                print(pkt.summary())

        print("**************STARTED***************")

        # Start sniffing on the specified interface with optional filters
        sniff(
            iface="Wi-Fi",  # Specify the network interface to sniff on
            prn=analyzer,  # Function to call for each captured packet
            filter=filter_    # Filter to capture only IP packets
            # You can use the following filters:
            # filter="icmp"  # Capture only ICMP packets
            # filter="tcp"   # Capture only TCP packets
            # filter="udp"   # Capture only UDP packets
            # filter="tcp port 80"  # Capture TCP packets on port 80 (HTTP)
            # filter="host 192.168.1.1"  # Capture packets from/to a specific IP address
        )


