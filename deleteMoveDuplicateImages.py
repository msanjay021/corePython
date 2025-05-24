import os
import shutil

def move_images(source_directory, destination_directory):
    # Iterate through all directories and subdirectories in the source directory
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            # Check if the file is an image file
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                # Construct the full path of the image file
                source_file_path = os.path.join(root, file)
                # Construct the destination path
                destination_file_path = os.path.join(destination_directory, file)
                # Check if the file exists
                if os.path.exists(source_file_path):
                    # Move the image file to the destination directory
                    shutil.move(source_file_path, destination_file_path)
                    print(f"Moved: {source_file_path}")
                else:
                    print(f"File not found: {source_file_path}")

# Source directory containing subfolders with image files
source_directory = r'D:\Ashu\phoneBackup'

# Destination directory where the images will be moved to
destination_directory = r'D:\Ashu\Optimized\DCIM'

# Call the function to move images
move_images(source_directory, destination_directory)

print("All images have been moved.")
