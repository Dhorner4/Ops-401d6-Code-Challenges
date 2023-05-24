#!/usr/bin/env python3
#Script: Ops 401 Class 28 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:05/24/2023
# Assistance from Chat GPT

# Main

import os
import ctypes
import logging
from cryptography.fernet import Fernet
from logging.handlers import RotatingFileHandler

# Setup logging
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Maximum log file size is 5 MB and we keep 5 backup files
log_file_handler = RotatingFileHandler('app.log', mode='a', maxBytes=5*1024*1024, 
                                        backupCount=5, encoding=None, delay=0)
log_file_handler.setFormatter(log_formatter)
log_file_handler.setLevel(logging.INFO)

# Setup StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
stream_handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_file_handler)
logger.addHandler(stream_handler)

def write_key():
    try:
        with open("key.key", "wb") as key_file:
            key_file.write(Fernet.generate_key())
        logger.info("Key written successfully.")
    except Exception as e:
        logger.error(f"Error occurred in write_key: {str(e)}")

def load_key():
    try:
        return open("key.key", "rb").read()
    except Exception as e:
        logger.error(f"Error occurred in load_key: {str(e)}")

# Your other functions with added logging and error handling...

# Test messages
logger.info("Info message test.")
logger.warning("Warning message test.")
logger.error("Error message test.")

while True:
    try:
        method_choice = input("Pick one of the following choices:\n1. Encrypt file\n2. Decrypt file\n3. Encrypt message\n4. Decrypt message\n5. Encrypt folder\n6. Decrypt folder\n7. Ransomware simulation\n8. Exit\n")
        if method_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            raise ValueError("Invalid choice.")
        # Rest of your logic...
    except Exception as e:
        logger.error(f"Error occurred in main loop: {str(e)}")
        print("An error occurred. Check the log for more information.")
# Done