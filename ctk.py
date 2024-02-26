from customtkinter import CTk
from customtkinter import CTkEntry, CTkButton
from pytube import YouTube
from tkinter import messagebox
# from bvPlayer import bvPlayer

def button_callback():
    print("button clicked")

app = CTk()
app.geometry("500x500")
app.resizable(False,False)

def downloadvid():
    url = txt_url.get()
    if len(url.strip()) < 1:
        messagebox.showerror('Invalid url', 'Please provide valid url')
    else:
        yt = YouTube(url=url)
        yt.streams.first().download
        
# enter url
txt_url = CTkEntry(app, placeholder_text='enter video url', width=350)
txt_url.place(x=50, y=30)

# btn download
btn_download = CTkButton(app, text='Download', command=downloadvid)
btn_download.place(x=120, y=80)

# button = w.CTkButton(app, text="my button", command=button_callback)
# button.pack(padx=20, pady=20)
# entry = w.CTkEntry(app, placeholder_text='Type here')
# entry.pack()

app.mainloop()