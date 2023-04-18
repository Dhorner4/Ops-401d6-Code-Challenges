#!/usr/bin/env python3
#Script: Ops 401 Class 02 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:04/18/2023
# Assistance from Chat GPT

# Main

import os, time
host = "192.168.3.1"

while True:
    response = os.system("ping -c 1 -W 1 " + host + " > /dev/null 2>&1")
    status = "Network Active" if response == 0 else "Network Down"
    print(time.strftime('%Y-%m-%d %H:%M:%S.%f'), status, "to", host)
    time.sleep(2)