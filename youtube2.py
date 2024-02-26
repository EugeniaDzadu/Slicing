from pytube import YouTube
from tkinter import Tk
from tkinter.ttk import *

window = Tk()
 
window.config(bg='#B2D7D7')
window.geometry('600x600+600+160')

def url():
    paste_url.get()
    yt = YouTube(f'{paste_url}', use_oauth=True)
    yt.streams.filter(progressive=True, file_extension='mp4').first().download()
    
    
paste_url = Entry(width=40)
search_vid = Button(text='Search', width=10)
watch_vid = Entry(width=40) 
Progress = Button(text='Download', width=10, command=url)





paste_url.place(x=50, y=20)
search_vid.place(x=320, y=20)
watch_vid.place(x=50, y=80, height=200)
Progress.place(x=50, y=300)
    
    
    
window.mainloop()