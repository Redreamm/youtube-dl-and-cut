from pydub import AudioSegment
from datetime import time

def cut_audio(input_file, output_file, start_time, end_time):
    # Load the audio file
    audio = AudioSegment.from_file(input_file, format="ogg", codec="libvorbis")

    # Convert start and end times to milliseconds
    start_time_ms = time_to_milliseconds(start_time)
    end_time_ms = time_to_milliseconds(end_time)

    # Cut the audio segment
    cut_segment = audio[start_time_ms:end_time_ms]

    # Save the cut segment to the output file
    cut_segment.export(output_file, format="ogg")

def time_to_milliseconds(time_str):
    time_str = str(time_str)
    # Split the time string into minutes and seconds
    minutes, seconds = map(int, time_str.split(':'))

    # Calculate the total time in milliseconds
    total_milliseconds = (minutes * 60 + seconds) * 1000
    return total_milliseconds