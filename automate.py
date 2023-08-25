import os
import shutil
import datetime

def organize_files(source_dir, destination_dir, log_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    now = datetime.datetime.now()
    log_file = os.path.join(log_dir, f"log_{now.strftime('%Y-%m-%d')}.txt")

    # Open the log file in append mode
    with open(log_file, "a") as log:
        log.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Script started\n")

        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            if os.path.isfile(source_path):
                file_extension = filename.split('.')[-1].lower()
                if file_extension in FILE_TYPES:
                    destination_path = os.path.join(destination_dir, FILE_TYPES[file_extension])
                    if not os.path.exists(destination_path):
                        os.makedirs(destination_path)
                    shutil.move(source_path, os.path.join(destination_path, filename))
                    log.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Moved {filename} to {destination_path} {EMOJIS[file_extension]}\n")
                else:
                    # Handle files with unlisted extensions
                    unlisted_folder = os.path.join(destination_dir, "OtherFiles")
                    if not os.path.exists(unlisted_folder):
                        os.makedirs(unlisted_folder)
                    shutil.move(source_path, os.path.join(unlisted_folder, filename))
                    log.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Moved {filename} to {unlisted_folder} 📁\n")

    # Log script completion
    with open(log_file, "a") as log:
        log.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Script finished\n")

# Define the source, destination, and log directories
source_directory = "../Downloads"
destination_directory = "../Destination"
log_directory = "../Destination/FileLogs"

# Define the file types and their respective destination folders
FILE_TYPES = {
    "pdf": "PDFs",
    "jpg": "Photos",
    "jpeg": "Photos",
    "png": "Photos",
    "txt": "TextFiles",
    "mp3": "Music",
    "mp4": "Videos",
    "dmg": "DMGs",
    "zip": "ZIPs"
}

# Define emojis for each file type
EMOJIS = {
    "pdf": "📄",
    "jpg": "📷",
    "jpeg": "📷",
    "png": "🖼️",
    "txt": "📝",
    "mp3": "🎵",
    "mp4": "🎥",
    "dmg": "💿",
    "zip": "📦"
}

# Automate file organization and logging
organize_files(source_directory, destination_directory, log_directory)
