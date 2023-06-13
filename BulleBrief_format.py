import os
import csv
import pandas as pd

sub_folder = 'cleaned_subtitles_mix2' # input your subtitle folder
summary_folder = 'summary_mix2' # input your clean summary folder
output_file = 'complete_data_mix2.csv' # input your output file
data = []

for sub_file in os.listdir(sub_folder):
    if sub_file.startswith('cleaned_'):
        summary_file = 'summary_' + sub_file
        if summary_file in os.listdir(summary_folder):
            with open(os.path.join(sub_folder, sub_file), 'r', encoding='utf-8') as f1, \
                 open(os.path.join(summary_folder, summary_file), 'r', encoding='utf-8') as f2:
                sub_text = f1.read().strip()
                summary_text = f2.read().strip()
            item = {
                'sub': sub_text,
                'summary': summary_text
            }
            data.append(item)
        else:
            print('Warning: Summary file not found for ' + sub_file)
    else:
        print('Warning: Unexpected sub file format for ' + sub_file)

df = pd.DataFrame(data)
df.to_csv(output_file, index=False)