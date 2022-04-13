# import win32clipboard
import argparse
import os

from pytube import YouTube
from pytube.cli import on_progress

from utils.functions import generate_clips
from utils.Menu import Menu


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
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-v", "--video", help="Link of the youtube video to download", required=True)
    # parser.add_argument("-c", "--cut", help="Timestamp range to cut, Format: [HH:]MM:SS,[HH:]MM:SS", required=True)
    # # parser.add_argument("--clipboard", help="Copies video link from clipboard")
    # # parser.add_argument("--file", help="Gets video and timestamps from a file")

    # args = parser.parse_args()
    # getClip(args.video, [args.cut.split(',')])
    menu = Menu({
        1: clipFromCli,
        2: clipsFromDesc,
        3: clipsFromFile
    })

    print(
    '''
    1) - Create clip from CLI argument
    2) - Create clips from video description
    3) - Create clips from file
    '''
    )
    menu.getOption()[int(input("Choose an option: "))]()

def clipFromCli():
    print("Creates clip from CLI arg")

def clipsFromDesc():
    print("Create clips from video desc")

def clipsFromFile():
    print("Creates clips from file")

# Downloads a video and generates a clip based on the timestamp range given
def getClip(videoURL: str, timeRange: list):
    try:
        # where to save
        save_path = "video"

        yt = YouTube(videoURL, on_progress_callback=on_progress)

        # print('Available formats :')
        # for stream in yt.streams.all():
        # print(stream)

        # itag = input('\nEnter the itag number to download video of that format: ')
        # stream = yt.streams.get_by_itag( itag )
        stream = yt.streams.get_highest_resolution()
        file_path = save_path + os.path.sep + stream.default_filename

        print('\nDownloading--- ' + yt.title + ' into location : ' + file_path)

        # desc_lines = yt.description.splitlines()
        # timeRange = convert_chapter_format_to_start_end_format(parse_lines(desc_lines))

        stream.download(save_path)
        generate_clips(file_path, timeRange)

        input('Hit Enter to exit')
    except Exception as e:
        print("Error", e)  # to handle exception
        input('Hit Enter to exit')


if __name__ == "__main__":
    main()
