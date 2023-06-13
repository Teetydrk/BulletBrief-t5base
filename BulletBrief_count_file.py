import os

folder_path = 'subtitles_mix'
num_files_subtitles_mix = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
print(f"The number of files in the folder {folder_path} is {num_files_subtitles_mix}")