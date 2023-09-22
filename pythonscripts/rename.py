import os

# Get the directory where the script is located
script_dir = os.path.dirname(__file__)

# Specify the folder containing the files (assuming it's in the same directory as the script)
folder_name = ""
folder_path = os.path.join(script_dir, folder_name)

# Specify the prefix you want to add
prefix = "accuracy_f_"

# Check if the folder exists
if os.path.exists(folder_path):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Create the new filename by adding the prefix
            new_filename = prefix + filename

            # Create the full file paths
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file with the new filename
            os.rename(old_file_path, new_file_path)

            print(f"Renamed: {filename} to {new_filename}")

    print("Prefix added to filenames for all files in the folder.")
else:
    print(f"Folder not found at path: {folder_path}")