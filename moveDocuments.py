import os
import shutil

def move_documents(source_directory, destination_directory):
    # Iterate through all directories and subdirectories in the source directory
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            # Check if the file is a document file
            if file.lower().endswith(('.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt')):
                # Construct the full path of the document file
                source_file_path = os.path.join(root, file)
                # Construct the destination path
                destination_file_path = os.path.join(destination_directory, file)
                # Check if the file exists
                if os.path.exists(source_file_path):
                    # Move the document file to the destination directory
                    shutil.move(source_file_path, destination_file_path)
                    print(f"Moved: {source_file_path}")
                else:
                    print(f"File not found: {source_file_path}")

# Source directory containing subfolders with document files
source_directory = r'D:\Ashu\Optimized'

# Destination directory where the document files will be moved to
destination_directory = r'D:\Ashu\phoneBackup\Documents'

# Call the function to move document files
move_documents(source_directory, destination_directory)

print("All document files have been moved.")
