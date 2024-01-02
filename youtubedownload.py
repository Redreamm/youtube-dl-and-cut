import yt_dlp

def download_video(link, name='%(title)s'):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', #берем самое лучшее качество видео и фото
        'outtmpl': 'video/{}.%(ext)s'.format(name), #наше выбраное имя
        'keepvideo': True,
        'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'vorbis',
    }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=True)
        downloaded_file_path = ydl.prepare_filename(info_dict)
    print(f"Видео {downloaded_file_path} успешно загружено!")
    return downloaded_file_path