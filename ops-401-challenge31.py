#!/usr/bin/env python3
#Script: Ops 401 Class 31 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:05/30/2023
# Assistance from Chat GPT

# Main


import os
import platform

def search_files(file_name, directory):
    file_count = 0
    hit_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:
                hit_count += 1
                file_path = os.path.join(root, file)
                print("Found:", file_path)
            file_count += 1

    print("Files searched:", file_count)
    print("Hits found:", hit_count)

def main():
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    if platform.system() == "Linux":
        command = "find " + directory + " -name " + file_name
        os.system(command)
    elif platform.system() == "Windows":
        command = 'dir /s /b "' + directory + '\\*' + file_name + '"'
        os.system(command)
    else:
        print("Unsupported operating system.")
        return

    print("\nSearching for files...")
    search_files(file_name, directory)

if __name__ == "__main__":
    main()

    # Done