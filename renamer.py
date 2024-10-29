import os

def rename_wav_files_in_current_directory():
    """
    Rename all .wav files in the current directory by removing spaces in their filenames.
    """
    current_directory = os.getcwd()  # Get the current working directory
    
    # Loop through all files in the current directory
    for filename in os.listdir(current_directory):
        # Check if the file is a .wav file
        if filename.endswith(".wav"):
            # Create a new filename by removing spaces
            new_filename = filename.replace(" ", "")
            
            # Get full file paths
            old_file = os.path.join(current_directory, filename)
            new_file = os.path.join(current_directory, new_filename)
            
            # Rename the file if the new name is different
            if old_file != new_file:
                os.rename(old_file, new_file)
                print(f"Renamed: {filename} -> {new_filename}")

# Example usage
rename_wav_files_in_current_directory()

