# Could have made this a format class with the functions as methods
from moviepy.editor import *
import os

def convert_to_mp3(video_file_path):
    mp4_file = rf'{video_file_path}.mp4'
    mp3_file = rf'{video_file_path}.mp3'

    videoclip = VideoFileClip(mp4_file)

    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()

def format_audio(audio_file_path):
    clip = AudioFileClip(audio_file_path) 

    if clip.duration < 14400:
        return clip
    else:
        num_cuts = clip.duration // 14400

        for i in range(num_cuts):
            clip = clip.subclip((14400 * i), (14400 * (i + 1)))
            new_fname = rf'file_path_part_{i}'
            clip.write_audiofile(new_fname)
        
    clip = clip.subclip((14400 * num_cuts), clip.duration)
    new_fname = rf'file_path_part_{num_cuts}'
    clip.write_audiofile(new_fname)

def format_directory(directory_path):
    list_of_files = os.listdir()

    for i in list_of_files:
        audio_file = convert_to_mp3(i)
        format_audio(audio_file)