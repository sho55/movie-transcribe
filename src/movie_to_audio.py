import os
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, audio_file):
    try:
        videoClip = VideoFileClip(video_path)
        audioClip = videoClip.audio

        converted_file = audioClip.write_audiofile(audio_file)
        print(converted_file)

    finally:
        if audioClip:
            audioClip.close()
        if videoClip:
            videoClip.close()

# 使用例
video_path = "/path/to/movieData"
audio_file = "./path/to/audioDataName"

extract_audio_from_video(video_path, audio_file)