import os
import tkinter as tk
from tkinter import messagebox, Button
from pytube import YouTube
import webbrowser

def search_videos():
    query = search_entry.get()
    search_response = youtube_search(query)

    video_listbox.delete(0, tk.END)

    for search_result in search_response.get("items", []):
        video_listbox.insert(tk.END, search_result["id"]["videoId"])

def play_video():
    selected_item = video_listbox.curselection()
    if selected_item:
        video_id = video_listbox.get(selected_item)
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        webbrowser.open(video_url)

def download_video():
    selected_item = video_listbox.curselection()
    if selected_item:
        video_id = video_listbox.get(selected_item)
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()

        download_folder = os.path.expanduser('~') + '/Downloads'
        video.download(download_folder)

        messagebox.showinfo("Success", "Video downloaded successfully!")

def youtube_search(query):
    # Replace with your actual YouTube Data API key
    api_key = "YOUR_YOUTUBE_API_KEY"
    youtube_service = build("youtube", "v3", developerKey=api_key)

    search_response = youtube_service.search().list(
        q=query,
        type="video",
        part="id",
        maxResults=10
    ).execute()

    return search_response

root = tk.Tk()
root.title("YouTube App")

search_label = tk.Label(root, text="Enter search query:")
search_label.pack()

search_entry = tk.Entry(root, width=40)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_videos)
search_button.pack()

video_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
video_listbox.pack()

play_button = tk.Button(root, text="Play", command=play_video)
play_button.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

root.mainloop()
