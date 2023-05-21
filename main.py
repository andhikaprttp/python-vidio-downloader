# import library 
from pytube import YouTube
from colorama import Fore
# Fungsi untuk mendownload video YouTube
def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # Menggunakan resolusi tertinggi
        video.download()  # Mendownload video
        print("Video berhasil didownload!")
    except Exception as e:
        print("Terjadi kesalahan saat mendownload video:", str(e))

print(Fore.GREEN + "=======================")
print(Fore.RED + "Hati hati penggunaan paket data")
print(Fore.GREEN + "=======================")
print(Fore.BLUE + "Youtube Vidio Downloader")
video_url = input("Masukan Link Vidio : ")
download_video(video_url)