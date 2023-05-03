#!/usr/bin/env python3
#Script: Ops 401 Class 13 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:05/03/2023
# Assistance from Chat GPT

# Main
import ipaddress
from scapy.all import IP, sr1, TCP, send

def tcp_port_scan(IP_add):
    # Define port range or specific set of ports to scan
    port_range = [22, 23, 80, 443, 3389]
    # Source port number
    source_port = 12345

    # Loop through each port in the range and scan for open, closed or filtered status
    for dsp_port in port_range:
        # Send the TCP SYN packet and receive the response
        response = sr1(IP(dst=IP_add)/TCP(sport=source_port, dport=dsp_port, flags="S"), timeout=1, verbose=0)

        # Check the response flags
        if response is not None and response.haslayer(TCP) and response[TCP].flags == 0x12:
            # If flag 0x12 received, send a RST packet to gracefully close the open connection
            rst_pkt = IP(dst=IP_add)/TCP(dport=dsp_port, sport=response[TCP].dport, flags="R")
            send(rst_pkt, verbose=0)
            print(f"Port {dsp_port} is open")
        elif response is not None and response.haslayer(TCP) and response[TCP].flags == 0x14:
            # If flag 0x14 received, notify user the port is closed
            print(f"Port {dsp_port} is closed")
        else:
            # If no flag is received, notify the user the port is filtered or silently dropped
            print(f"Port {dsp_port} is filtered or silently dropped")

def network_scan(IP_add):
    response = sr1(IP(dst=IP_add)/ICMP(), timeout=1, verbose=0)
    if response is not None and response.type == 0 and response.code == 0:
        print(f"{IP_add} is up")
        tcp_port_scan(IP_add)
    elif response is not None and response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
        print(f"{IP_add} is actively blocking ICMP traffic")
    else:
        print(f"{IP_add} is down or unresponsive")

# Prompt user for target IP address
IP_add = input("Please type in an IP address: ")

network_addr = ipaddress.ip_network(IP_add, strict=False)
hosts = list(network_addr.hosts())

up_hosts = []
for host in hosts:
    if str(host) == str(network_addr.network_address) or str(host) == str(network_addr.broadcast_address):
        continue
    network_scan(str(host))

print(f"{len(up_hosts)} hosts are online")