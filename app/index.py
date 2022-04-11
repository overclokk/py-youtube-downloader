# import win32clipboard
from functions import get_seconds
from pytube.cli import on_progress
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import argparse
import os


# https://superuser.com/questions/1567253/how-to-download-chapters-of-a-youtube-video-as-separate-video-files

# https://medium.com/daily-python/python-script-to-download-youtube-videos-daily-python-6-c3788be5b6b1
# try:
#     # get clipboard data
#     win32clipboard.OpenClipboard()
#     link = win32clipboard.GetClipboardData()
#     win32clipboard.CloseClipboard()
# except Exception as ex:
#     print('Error : ', ex )
#     exit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video", help="Link of the youtube video to download", required=True)
    parser.add_argument("-c", "--cut", help="Timestamp range to cut, Format: [HH:]MM:SS,[HH:]MM:SS", required=True)
    # parser.add_argument("--clipboard", help="Copies video link from clipboard")
    # parser.add_argument("--file", help="Gets video and timestamps from a file")

    args = parser.parse_args()
    getClip(args.video, args.cut)


# Downloads a video and generates a clip based on the timestamp range given
def getClip(videoURL: str, timeRange: str):
    try:
        # where to save
        save_path = "video"

        yt = YouTube(videoURL, on_progress_callback=on_progress)
        # timeCuts = getTimestamps(timeRange)
        # timeCuts = get_seconds(timeRange.split(','))
        # print('Available formats :')
        # for stream in yt.streams.all():
        # print(stream)

        # itag = input('\nEnter the itag number to download video of that format: ')
        # stream = yt.streams.get_by_itag( itag )
        stream = yt.streams.get_highest_resolution()
        file_path = save_path + os.path.sep + stream.default_filename

        print('\nDownloading--- ' + yt.title + ' into location : ' + file_path)
        stream.download(save_path)

        time = timeRange.split(',')
        ffmpeg_extract_subclip(
            file_path,
            get_seconds( time[0] ),
            get_seconds( time[1] ),
            targetname="clip.mp4"
        )

        input('Hit Enter to exit')
    except Exception as e:
        print("Error", e)  # to handle exception
        input('Hit Enter to exit')


# Separates timestamp range
def getTimestamps(timeRange):
    return timeRange.rsplit(":")


if __name__ == "__main__":
    main()
