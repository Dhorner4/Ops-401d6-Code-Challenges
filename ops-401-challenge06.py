#!/usr/bin/env python3
#Script: Ops 401 Class 06 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:04/24/2023
# Assistance from Chat GPT

# Main
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

def encrypt_message(message, key):
    encrypted = Fernet(key).encrypt(message.encode('utf-8'))
    print("The encrypted message is:", encrypted.decode('utf-8'))

def decrypt_message(encrypted_message, key):
    decrypted = Fernet(key).decrypt(encrypted_message.encode('utf-8'))
    print("The decrypted message is:", decrypted.decode('utf-8'))

write_key()

while True:
    method_choice = input("Pick one of the following choices:\n1. Encrypt file\n2. Decrypt file\n3. Encrypt message\n4. Decrypt message\n5. Exit\n")
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
        break
    else:
        print("Choose is invalid. Please try again.")

    # Done