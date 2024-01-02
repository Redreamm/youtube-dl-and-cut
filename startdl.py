import pandas as pd
import re
import youtubedownload
import cutaudio

df = pd.read_excel('table_quiz.xlsx')

for index, row in df.iterrows():
    youtube_link = row['yotubelink']

    if pd.isnull(youtube_link) or not youtube_link.strip():  # Check if it's NaN or an empty/whitespace string
        print('row ', row['correct'], ' skipped')
        continue
    filename = row['correct']
    filename = re.sub(r'\s+', '-', filename)
    start_time = row['starttime']
    end_time = row['endtime']

    if youtube_link.isspace() or youtube_link == '' or pd.isnull(youtube_link):  # Skip if the cell is empty or contains only whitespaces
        print('row ',filename,' skipped')
        continue

    # Download the YouTube video
    youtubedownload.download_video(youtube_link, filename)

    # Cut the audio
    input_file = f'video/{filename}.ogg'
    output_file = f'cuted/{filename}.ogg'
    cutaudio.cut_audio(input_file, output_file, start_time, end_time)
    print('audio ',filename,' ready')