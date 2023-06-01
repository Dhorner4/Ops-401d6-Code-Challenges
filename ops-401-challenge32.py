#!/usr/bin/env python3
#Script: Ops 401 Class 32 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:05/31/2023
# Assistance from Chat GPT

# Main

import os
import platform
import hashlib
import time

def search_files(file_name, directory):
    file_count = 0
    hit_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:
                hit_count += 1
                file_path = os.path.join(root, file)
                
                # Calculate MD5
                md5_hash = hashlib.md5()
                with open(file_path,"rb") as f:
                    for byte_block in iter(lambda: f.read(4096),b""):
                        md5_hash.update(byte_block)
                md5 = md5_hash.hexdigest()

                # Get file size
                file_size = os.path.getsize(file_path)
                
                # Get current time
                timestamp = time.ctime()

                print(f"Timestamp: {timestamp}, File: {file_path}, Size: {file_size}, MD5: {md5}")
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
