import os
import yt_dlp

def download_video(link, id, video_quality):
    youtube_dl_options = {
        'format': video_quality,
        "outtmpl": os.path.join(os.getcwd(), f"{id}.mp4"),
    }

    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        try:
            ydl.download([link])
        except yt_dlp.utils.DownloadError as e:
            print(f"Error downloading video: {e}")

def download_audio(link, id):
    youtube_dl_options = {
        "format": "bestaudio/best",
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        "outtmpl": os.path.join(os.getcwd(), f"{id}.mp3"),
    }

    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        try:
            ydl.download([link])
        except yt_dlp.utils.DownloadError as e:
            print(f"Error downloading audio: {e}")

def main():
    youtube_url = input("Enter the YouTube URL: ")
    choice = input("Enter 'v' to download video or 'a' to download audio: ")

    if choice == 'v':
        video_quality = input("Enter the desired video quality (e.g., 'best' or '1080'): ")
        download_video(youtube_url, 'video_id', video_quality)
    elif choice == 'a':
        download_audio(youtube_url, 'audio_id')
    else:
        print("Invalid choice. Please enter 'v' for video or 'a' for audio.")

if __name__ == "__main__":
    main()
