import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import tempfile


class App(tk.Tk):
   def __init__(self):
       super().__init__()

       self.title("TikTok Video Viewer")
       self.geometry("400x300")

       self.entry = tk.Entry(self, width=50)
       self.entry.pack(pady=10)

       self.button = tk.Button(self, text="View Video", command=self.view_video)
       self.button.pack(pady=10)

   def view_video(self):
       url = self.entry.get()

       if not url:
           messagebox.showerror("Error", "Please enter a valid URL.")
           return

       try:
           self.download_video(url)
           self.open_video()
       except Exception as e:
           messagebox.showerror("Error", str(e))

   def download_video(self, url):
       command = f"youtube-dl -f bestvideo+bestaudio -o '%(title)s.%(ext)s' {url}"
       with tempfile.TemporaryDirectory() as tmpdirname:
           os.chdir(tmpdirname)
           subprocess.check_output(command, shell=True)
           downloaded_file = os.listdir(tmpdirname)[0]
           self.downloaded_video_path = os.path.join(tmpdirname, downloaded_file)

   def open_video(self):
       os.startfile(self.downloaded_video_path)


if __name__ == "__main__":
   app = App()
   app.mainloop()