import os
import shutil

def organize_files_by_name(source_dir):
    """
    Organizes files in the source directory into folders based on their names.

    Parameters:
    source_dir (str): The path to the directory containing the files to organize.

    """
    if not os.path.exists(source_dir):
        print(f"The directory {source_dir} does not exist.")
        return

    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Skip directories
        if not os.path.isfile(file_path):
            continue

        # Extract the prefix or part of the file name as folder name
        # Example: For "PXL_20241116_093803415.jpg", use "PXL" as folder name
        folder_name = filename.split('_')[0]  # Modify the delimiter if needed
        folder_path = os.path.join(source_dir, folder_name)

        # Ensure the folder is created
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        except Exception as e:
            print(f"Error creating folder {folder_path}: {e}")
            continue

        # Move the file into the folder
        try:
            shutil.move(file_path, os.path.join(folder_path, filename))
        except Exception as e:
            print(f"Error moving file {filename}: {e}")

    print(f"Files in {source_dir} have been organized into folders.")

# Example usage
source_directory = r"C:\Users\Swetha\Downloads\SampleFolder"  # Replace with your directory path
organize_files_by_name(source_directory)
