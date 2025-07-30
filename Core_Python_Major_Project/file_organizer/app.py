import os
import shutil
from datetime import datetime
from type import FILE_TYPES


def get_category(extension):
    for category, ext_list in FILE_TYPES.items():
        if extension.lower() in ext_list:
            return category
    return 'Others'


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def organize_files(source_folder):
    files = os.listdir(source_folder)
    log_entries = []

    for file in files:
        file_path = os.path.join(source_folder, file)
        
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            category = get_category(ext)
            target_folder = os.path.join(source_folder, category)
            
            create_folder(target_folder)
            
            target_path = os.path.join(target_folder, file)
            
            try:
                shutil.move(file_path, target_path)
                log_entries.append(f"{datetime.now()} - Moved: {file} → {category}")
            except Exception as e:
                log_entries.append(f"{datetime.now()} - ERROR moving {file}: {str(e)}")
    
    write_log(log_entries)
    print("✅ Organizing complete. Check log for details.")

def write_log(logs):
    with open("organizer_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write("\n".join(logs) + "\n")


if __name__ == "__main__":
    folder = input("📁 Enter the folder path to organize: ").strip()
    
    if os.path.exists(folder):
        organize_files(folder)
    else:
        print("❌ Invalid path. Please try again.")
