import os

# Specify the directory path where you want to delete files
directory = r"D:\Ashu\phoneBackup\Music"

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the filename contains "(1)"
    if "(1)" in filename:
        # Construct the full file path
        filepath = os.path.join(directory, filename)
        # Check if the file exists
        if os.path.isfile(filepath):
            # Delete the file
            os.remove(filepath)
            print(f"Deleted: {filename}")
        else:
            print(f"File not found: {filename}")
