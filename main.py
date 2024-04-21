import tkinter
import customtkinter
from pytube import YouTube
from tkinter import filedialog

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        output_path = filedialog.askdirectory()
        video.download(output_path=output_path)
        finished.configure(text="Download Complete")
    except Exception as e:
        finished.configure(text="Error")

def on_progress(stream, chunk, byte_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - byte_remaining
    percentage_of_competetion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_competetion))
    progress.configure(text=per + '%')
    progress.update()
    progressbar.set(float(percentage_of_competetion) / 100)


#System Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#UI Element
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Finished Downloading
finished = customtkinter.CTkLabel(app, text="")
finished.pack(padx=10, pady=10)

#Progress Percentage
progress = customtkinter.CTkLabel(app, text='0%')
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)


#Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)


#Run App
app.mainloop()