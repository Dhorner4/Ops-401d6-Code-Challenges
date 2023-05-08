#!/usr/bin/env python3
#Script: Ops 401 Class 16 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:05/08/2023
# Assistance from Chat GPT

# Main
import time

# Prompt the user to select a mode
mode = input("Select a mode (1 for Offensive, 2 for Defensive): ")

if mode == "1":
    # Offensive mode: iterate through word list file and print each word with a delay
    word_list_path = input("Enter path to word list file: ")
    with open(word_list_path, 'r') as f:
        for line in f:
            word = line.strip()
            print(word)
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
        
else:
    print("Invalid mode selected.")
    # Done