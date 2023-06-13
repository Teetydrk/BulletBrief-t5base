import openai
import os
from tqdm import tqdm
import time

openai.api_key = "sk-" # input your own openai api key

input_folder_path = "cleaned_subtitles_mix" # input your input folder
output_folder_path = "summary_mix" # input your output folder

os.makedirs(output_folder_path, exist_ok=True)

while True:
    for filename in tqdm(os.listdir(input_folder_path)):
        if filename not in output_folder_path:
            input_file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(output_folder_path, f'summary_{filename}')
            if os.path.exists(output_file_path):
                print(f"{filename} has already been processed. Skipping.")
                continue
            with open(input_file_path, "r", encoding="utf-8") as input_file, \
                 open(output_file_path, "w", encoding="utf-8") as output_file:
                text = input_file.read()
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": f"Summarize the following text in bullet points: \n{text}"}], 
                    )
                    summary = response.choices[0].message.content.strip()
                    output_file.write(summary)
                    time.sleep(15)
                except openai.error.InvalidRequestError:
                    print(f"{filename} was skipped due to exceeding the token limit.")
                    os.remove(input_file_path)
                    continue