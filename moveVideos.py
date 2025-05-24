import os
import shutil

def move_videos(source_directory, destination_directory):
    # Iterate through all directories and subdirectories in the source directory
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            # Check if the file is a video file (you can add more extensions if needed)
            if file.endswith(('.mp4', '.avi', '.mov', '.mkv', '.wmv')):
                # Construct the full path of the video file
                source_file_path = os.path.join(root, file)
                # Check if the file exists
                if os.path.exists(source_file_path):
                    # Construct the destination path
                    destination_file_path = os.path.join(destination_directory, file)
                    # Check if the file already exists in the destination directory
                    if os.path.exists(destination_file_path):
                        # If the file exists, remove it
                        os.remove(destination_file_path)
                        print(f"Replaced: {destination_file_path}")
                    # Move the video file to the destination directory
                    shutil.move(source_file_path, destination_directory)
                    print(f"Moved: {source_file_path}")
                else:
                    print(f"File not found: {source_file_path}")

# Source directory containing subfolders with video files
source_directory = r'D:\Ashu\phoneBackup'

# Destination directory where the videos will be moved to
destination_directory = r'D:\Ashu\Optimized\Videos'

# Call the function to move videos
move_videos(source_directory, destination_directory)

print("All videos have been moved.")
