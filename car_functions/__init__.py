import os

# check the current files and folders
files_folders = os.listdir()

# check if a 'data' folder is in the list
if 'data' not in files_folders:
    print("📂 Creating data folder")
    os.mkdir('data')
    print("✅ Created data folder")