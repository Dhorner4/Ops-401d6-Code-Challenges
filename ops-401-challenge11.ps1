#!/usr/bin/env python3
#Script: Ops 401 Class 11 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:05/01/2023
# Assistance from Chat GPT

# Main

# Scapy tool activation
from scapy.all import IP, sr1, TCP

# Define host IP
IP_add = input("Please type in an IP address: ")
# Define port range or specific set of ports to scan
port_range = [22, 23, 80, 443, 3389]
# Source port number
source_port = int(input("Enter source port number: "))

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

        # Done