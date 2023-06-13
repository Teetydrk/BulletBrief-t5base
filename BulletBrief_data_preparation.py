import os
from youtube_transcript_api import YouTubeTranscriptApi
from tqdm import tqdm

input_file = 'links.txt' # input your link file
output_folder = 'subtitles_mix' # input your output file

def get_subtitle(link):
    try:
        video_id = link.split("v=")[1]
        subtitle = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        subtitle_text = " ".join([s['text'] for s in subtitle])
        return subtitle_text
    except:
        return "Subtitle not found"
    
def save_subtitle_to_file(subtitle_text, filename):
    subtitle_text = subtitle_text.replace('\n', ' ')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(subtitle_text)

def get_all_subtitles_from_file(file_path, output_folder):
    with open(file_path, 'r') as file:
        links = file.readlines()

    for link in tqdm(links, desc="Processing videos"):
        link = link.strip()
        subtitle_text = get_subtitle(link)
        if subtitle_text != "Subtitle not found":
            video_id = link.split("v=")[1]
            filename = f"subtitle_{video_id}.txt"
            output_path = os.path.join(output_folder, filename)
            save_subtitle_to_file(subtitle_text, output_path)

os.makedirs(output_folder, exist_ok=True)
get_all_subtitles_from_file(input_file, output_folder)