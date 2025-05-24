import os
import shutil

def move_images(source_folder):
    # Traverse the directory and its subdirectories
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Check if the file is an image
            if any(file.lower().endswith(image_ext) for image_ext in ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff')):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(source_folder, file)
                shutil.move(source_path, destination_path)
                print(f"Moved: {source_path} -> {destination_path}")

def main():
    # Edit the source folder here
    source_folder = r"D:\Ashu\phoneBackup\DCIM"

    # Check if source folder exists
    if not os.path.isdir(source_folder):
        print("Source folder does not exist.")
        return

    # Move images from subfolders to the source folder
    move_images(source_folder)

if __name__ == "__main__":
    main()
