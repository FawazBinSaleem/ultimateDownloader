
from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = input("enter a url: ")
 
video= YouTube(url, on_progress_callback = on_progress)
print(video.title)
 
progress = video.streams.get_highest_resolution()
progress.download()