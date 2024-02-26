from pytube import YouTube

yt = YouTube('https://youtu.be/in1uxSpvsw0', use_oauth=True)
yt.streams.filter(progressive=True, file_extension='mp4').first().download()
