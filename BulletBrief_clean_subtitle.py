import os
import re

input_folder_path = 'subtitles_mix2'
output_folder_path = 'cleaned_subtitles_mix2'

os.makedirs(output_folder_path, exist_ok=True)

for filename in os.listdir(input_folder_path):
    input_file_path = os.path.join(input_folder_path, filename)
    output_file_path = os.path.join(output_folder_path, f'cleaned_{filename}')
    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file:
        lines = input_file.readlines()
        del lines[:4]
        contents = ''.join(lines)
        pattern = re.compile(r'\d{2}:\d{2}:\d{2}.\d{3} --> \d{2}:\d{2}:\d{2}.\d{3}')
        cleaned_contents = re.sub(pattern, '', contents)
        cleaned_contents = re.sub(r'<.*?>', '', cleaned_contents)
        cleaned_contents = re.sub(r'align:start position:\d+% line:\d+%', '', cleaned_contents)
        cleaned_contents = re.sub(r'Transcriber: .*', '', cleaned_contents)
        cleaned_contents = re.sub(r'Translator: .*', '', cleaned_contents)
        cleaned_contents = re.sub(r'Reviewer: .*', '', cleaned_contents)
        cleaned_contents = re.sub(r'\([^()]*\)', '', cleaned_contents)
        cleaned_contents = cleaned_contents.replace('\n', ' ')
        cleaned_contents = ' '.join(cleaned_contents.split())

        if '♫' in cleaned_contents:
            output_file.close()
            os.remove(output_file_path)
            print(f"Deleted file containing ♫ character : {output_file_path} ")
        else:
            output_file.write(cleaned_contents)
            output_file.seek(0, os.SEEK_END)
            if output_file.tell() == 0:
                output_file.close()
                os.remove(output_file_path)
                print(f"Deleted empty file : {output_file_path}")

num_files = len(os.listdir(output_folder_path))
print(f"Number of files in output folder: {num_files}")