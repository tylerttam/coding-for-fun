import os
import shutil

# 👇 change this to your real Downloads path
DOWNLOADS_PATH = "/Users/tylertam/Downloads"

# Define file categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".heic"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
}

# Create folders if they don't exist
for folder in FILE_TYPES.keys():
    folder_path = os.path.join(DOWNLOADS_PATH, folder)
    os.makedirs(folder_path, exist_ok=True)

# Loop through all files
for filename in os.listdir(DOWNLOADS_PATH):
    file_path = os.path.join(DOWNLOADS_PATH, filename)

    # Skip folders and the script itself
    if os.path.isdir(file_path) or filename == os.path.basename(__file__):
        continue

    # Check file extension and move accordingly
    file_ext = os.path.splitext(filename)[1].lower()

    moved = False
    for folder, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            dest_path = os.path.join(DOWNLOADS_PATH, folder, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved {filename} → {folder}/")
            moved = True
            break

    # Optional: if extension not recognized, put in 'Other'
    if not moved:
        other_folder = os.path.join(DOWNLOADS_PATH, "Other")
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(other_folder, filename))
        print(f"Moved {filename} → Other/")
