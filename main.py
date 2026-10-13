import os
import hashlib
import csv

print("=== File System Investigator ===")

def calculate_sha256(full_path): # Calculate the SHA-256 hash of a file  

    try:
        sha256_hash = hashlib.sha256()

        with open(full_path, "rb") as file: # Open the file in binary read mode

            for chunk in iter(lambda: file.read(4096), b""): # Read the file in chunks
                 sha256_hash.update(chunk)

        return sha256_hash.hexdigest() # Return the final hash a hexadecimal string

    except OSError as error:
        print("[ERROR] Could not hash file:", full_path) #Display an error if the file cannot be read
        print("Reason", error) # Display the reason the file could not be read
        return None # Return None to indicate that hashing failed


print("Operating System:", os.name) # Display the operating system interface Python is using


print("Current Directory:", os.getcwd()) # Display the current working directory


directory = input("Enter a directory path to scan: ") # Ask the user to enter a directory path to scan


if os.path.isdir(directory): # Check whether the selected directory exists

    risky_extensions = [".exe", ".bat", ".ps1", ".vbs", ".scr"] # File exstensions that deserve a security review

    print("\nFiles and folders in this directory:") # Display a heading before listing the results
    print("Security check: scanning file exstensions...")

    with open("scan_report.csv", "w", newline="", encoding="utf-8") as report: # Set up a report to store the scan results
                
        writer = csv.writer(report)
                
        writer.writerow([
            "Filename",
            "Full Path",
            "Size (bytes)",
            "SHA-256",
            "Review Required"
        ])


        for current_directory, subdirectories, files in os.walk(directory):  # Loop through each item in the directory

            for item in files:
                full_path = os.path.abspath(os.path.join(current_directory, item))  # Get the absolute path of the current item

                extension = os.path.splitext(item)[1].lower() # Get the file exstension and convert it to lowercase

                review_required = extension in risky_extensions

                if review_required:  # Check if the file has a potentially risky extension
                    print("[REVIEW] Potentially risky file:", item)  # Display a warning

                if os.path.isfile(full_path):  # Check whether the current path points to a file

                    try:  # Attempt to retrieve the file information
                        size = os.path.getsize(full_path)  # Get the file size in bytes
                        print("[FILE]", full_path, "| Size:", size, "bytes")  # Display the file path and size

                        file_hash = calculate_sha256(full_path)  # Calculate the SHA-256 hash

                        if file_hash is not None:  # Check whether hashing succeeded
                            print("SHA-256:", file_hash)  # Display the hash
                        else:  # Handle an unsuccessful hash calculation
                            print("SHA-256: Could not calculate hash")  # Display an error message

                        writer.writerow([  # Write the file details into the CSV report
                            item,
                            full_path,
                            size,
                            file_hash if file_hash is not None else "Hash unavailable",
                            "Yes" if review_required else "No"
                            ])

                    except OSError as error:  # Handle errors accessing the file
                        print("[ERROR] Could not inspect file:", full_path)  # Display the file path
                        print("Reason:", error)  # Display the reason for the error

