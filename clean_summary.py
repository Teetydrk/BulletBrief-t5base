import os

folder_path = "summary_mix"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("•", "-")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)


num_files = len(os.listdir(folder_path))
print(f"Number of files in output folder: {num_files}")