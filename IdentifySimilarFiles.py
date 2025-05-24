import os
import hashlib

def hash_file(file_path):
    """Calculate the hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def find_matching_files(directory):
    # Dictionary to store file hashes as keys and their paths as values
    file_dict = {}

    # Traverse the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)

            # Add the file to the dictionary if the hash is not already present
            if file_hash not in file_dict:
                file_dict[file_hash] = file_path

    return file_dict

def main():
    # Edit the directory path here
    directory = "D:/Ashu/phoneBackup"

    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    unique_files = find_matching_files(directory)

    if unique_files:
        print("Duplicate files found:")
        for file_hash, file_path in unique_files.items():
            print(f"File: {file_path}")
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()
