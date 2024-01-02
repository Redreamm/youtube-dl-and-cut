import pandas as pd
import re
import youtubedownload
import cutaudio

df = pd.read_excel('table_quiz.xlsx')

# Start from column "correct" and cell contains 'Harpy eagle'
desired_row_index = df[df['correct'] == 'Ring-tailed lemur'].index[0]

for index, row in df.iterrows():
    if index < desired_row_index:
        continue

    youtube_link = row['yotubelink']

    if pd.isnull(youtube_link) or not youtube_link.strip():
        print('row', row['correct'], 'skipped')
        continue
    filename = row['correct']
    # Ensure filename is a string
    filename = str(filename)
    filename = re.sub(r'\s+', '-', filename)
    print('Называние животного' + filename)
    start_time = row['starttime']
    end_time = row['endtime']

    if youtube_link.isspace() or youtube_link == '' or pd.isnull(youtube_link):
        print('row', filename, 'skipped')
        continue

    # Download the YouTube video
    youtubedownload.download_video(youtube_link, filename)

    # Cut the audio
    input_file = f'video/{filename}.ogg'
    output_file = f'cuted/{filename}.ogg'
    cutaudio.cut_audio(input_file, output_file, start_time, end_time)
    print('audio', filename, 'ready')
