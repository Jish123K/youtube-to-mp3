import os

import moviepy.editor as mp

import tkinter as tk

from tkinter import filedialog, messagebox

class Application(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)

        self.master = master

        self.master.title('YouTube MP3 Downloader')

        self.master.geometry('700x200')

        self.create_widgets()

    def create_widgets(self):

        # Link input line

        self.url_label = tk.Label(self.master, text='Video link (ctrl+v):', font=(None, 12))

        self.url_label.place(x=40, y=60)

        self.url_entry = tk.Entry(self.master, width=50)

        self.url_entry.place(x=210, y=61)

        # Path line

        self.folder_path = tk.StringVar()

        self.path_label = tk.Label(self.master, text='Save mp3 to:', font=(None, 12))

        self.path_label.place(x=40, y=90)

        self.path_entry = tk.Entry(self.master, width=50, textvariable=self.folder_path)

        self.path_entry.place(x=210, y=91)

        # Browse button

        self.brws_button = tk.Button(self.master, text='Browse', command=self.browse_button)

        self.brws_button.place(x=580, y=85)

        # Download button

        self.down_button = tk.Button(self.master, text='Download', command=self.download_video)

        self.down_button.place(x=40, y=150)

    def browse_button(self):

        self.folder_path.set(filedialog.askdirectory())

    def download_video(self):

        video_link = self.url_entry.get().strip()

        save_path = self.folder_path.get().strip()

        if not video_link.startswith(('http://', 'https://')):

            messagebox.showerror('Error', 'Please enter a valid video link.')

            return

        elif not save_path:

            messagebox.showerror('Error', 'Please choose a directory to save the MP3 file.')

            return

        # Download video

        try:

            messagebox.showinfo('Downloading', 'Downloading video...')

            video = mp.VideoFileClip(video_link)

            audio = video.audio

            audio.write_audiofile(os.path.join(save_path, 'audio.mp3'))

            messagebox.showinfo('Success', 'MP3 file has been saved to the specified directory.')

        except Exception as e:

            messagebox.showerror('Error', f'Something went wrong.\n\n{e}')

if __name__ == '__main__':

    root = tk.Tk()

    app = Application(master=root)

    app.mainloop()

