#!/usr/bin/env python3
#Script: Ops 401 Class 03 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:04/19/2023
# Assistance from Chat GPT

# Main

#Import Libraries
import smtplib
import datetime, time, os
from getpass import getpass

# Declare variables
up = "Network is active"
down = "Network is down"
email = input("please type your email:")
password = getpass("please provide your password:")
ip = ("ip address:")

# Ping
def ping_Status(ip):
    # Evaluate the response and assign success or failure to the status variable
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        status = up 
    else:
        status = down
    return status

# send email if status changes
def send_email(status):
    # Create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # Start TLS for security
    s.starttls()

    # Authentication
    s.login(email, password)

    # Message to be sent
    message = f"Your network is {status.lower()}"
    s.sendmail(email, email, message)

    # Terminate the session
    s.quit()

# Initial ping status
last_status = ping_Status(ip)

while True:
    # Transmit a single ICMP ping packet to the target
    current_status = ping_Status(ip)
    # If status has changed, send an email
    if current_status != last_status:
        send_email(current_status)
        last_status = current_status
    # Wait for 2 seconds before transmitting another ping packet
    time.sleep(2) 
# end


