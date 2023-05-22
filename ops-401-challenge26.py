#!/usr/bin/env python3
#Script: Ops 401 Class 26 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:05/22/2023
# Assistance from Chat GPT

import os
import ctypes
import logging
from cryptography.fernet import Fernet

# Main
# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def write_key():
    try:
        with open("key.key", "wb") as key_file:
            key_file.write(Fernet.generate_key())
        logging.info("Key written successfully.")
    except Exception as e:
        logging.error(f"Error occurred in write_key: {str(e)}")

def load_key():
    try:
        return open("key.key", "rb").read()
    except Exception as e:
        logging.error(f"Error occurred in load_key: {str(e)}")

# Your other functions with added logging and error handling...

while True:
    try:
        method_choice = input("Pick one of the following choices:\n1. Encrypt file\n2. Decrypt file\n3. Encrypt message\n4. Decrypt message\n5. Encrypt folder\n6. Decrypt folder\n7. Ransomware simulation\n8. Exit\n")
        if method_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            raise ValueError("Invalid choice.")
        # Rest of your logic...
    except Exception as e:
        logging.error(f"Error occurred in main loop: {str(e)}")
        print("An error occurred. Check the log for more information.")
        
        # done
