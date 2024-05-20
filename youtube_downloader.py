from pytube import YouTube
import tkinter as tk   #gui smth in python
from tkinter import filedialog

def download_video (url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension = 'mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print('Видео успешно загружено!')

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')

    return folder
if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    video_url = input('Пожалуйста вставьте линку на видос с Ютуба: ')
    save_directory = open_file_dialog()

    if save_directory:
        print('Загрузка началась...')
        download_video(video_url, save_directory)
    else:
        print('Некорректное место для хранения')
        
