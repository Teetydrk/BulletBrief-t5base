import os
from tqdm import tqdm

folder_path = "summary_mix"
old_folder_path = "summary_mix"

file_list = os.listdir(folder_path)
old_file_list = os.listdir(old_folder_path)

for file in tqdm(file_list):
    file_path = os.path.join(folder_path, file)
    if os.path.getsize(file_path) == 0:
        os.remove(file_path)
        print(f"Deleted {file_path}")