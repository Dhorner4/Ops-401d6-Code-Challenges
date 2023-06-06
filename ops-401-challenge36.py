#!/usr/bin/env python3
#Script: Ops 401 Class 36 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:06/06/2023
# Assistance from Chat GPT

# Main

import os

# Prompt the user to enter a URL or IP address
target = input("Enter a URL or IP address: ")

# Prompt the user to enter a port number
port = input("Enter a port number: ")

# Perform banner grabbing using netcat
print("Netcat Banner Grabbing Results:")
os.system(f"nc -v {target} {port}")

# Perform banner grabbing using telnet
print("\nTelnet Banner Grabbing Results:")
os.system(f"telnet {target} {port}")

# Perform banner grabbing using Nmap
print("\nNmap Banner Grabbing Results:")
os.system(f"nmap -p- -sV {target}")

# Perform banner grabbing using WhatWeb
print("\nWhatWeb Banner Grabbing Results:")
os.system(f"whatweb {target}")

# Perform banner grabbing using CURL
print("\nCURL Banner Grabbing Results:")
os.system(f"curl -I {target}")

# Done