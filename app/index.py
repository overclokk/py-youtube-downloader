# import win32clipboard
# import argparse
import os
import glob

from pytube import YouTube
from pytube.cli import on_progress
from http.client import IncompleteRead

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
        1: download_video,
        2: create_clip_from_cli_arguments,
        3: create_clips_from_video_chapters,
        4: create_clips_from_text_file,
        5: create_clips_from_downloaded_video
    })

    print(
        '''
        1) - Download video
        2) - Create clip from CLI argument
        3) - Create clips from video description
        4) - Create clips from file
        5) - Create clips from downloaded video
        '''
    )

    menu.getOption()[int(input("Choose an option: "))]()


# TODO: implement
def download_video():
    print("Download the video")
    input("Insert the clip time range in `[HH:]MM:SS,[HH:]MM:SS` format: ")


# Gets a single clip from video
def create_clip_from_cli_arguments() -> None:
    get_clip(
        input("Insert video link: "),
        [input("Insert clip time range [HH:]MM:SS,[HH:]MM:SS: ").split(',')]
    )


# TODO: implement
def create_clips_from_video_chapters() -> None:
    print("Create clips from video desc")


# TODO: implement
def create_clips_from_text_file() -> None:
    print("Creates clips from file")


def create_clips_from_downloaded_video() -> None:
    files = glob.glob('video' + os.path.sep + '*.mp4')
    for i, name in enumerate(files):
        print(f'{i}) - ' + name)

    selected_video = int(input("Select video by index: "))
    generate_clips(
        files[selected_video],
        [input("Insert clip time range [HH:]MM:SS,[HH:]MM:SS: ").split(',')]
    )


# TODO: Refactor it in a way to be able to use a single function for all options
# Downloads a video and generates a clip based on the timestamp range given
def get_clip(video_url: str, time_range: list) -> None:
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)

        # print('Available formats :')
        # for stream in yt.streams.all():
        # print(stream)

        # itag = input('\nEnter the itag number to download video of that format: ')
        # stream = yt.streams.get_by_itag( itag )
        stream = yt.streams.get_highest_resolution()

        # where to save
        save_path = "video"
        file_path = save_path + os.path.sep + stream.default_filename

        print('\nDownloading--- ' + yt.title + ' into location : ' + file_path)

        stream.download(save_path)

        # desc_lines = yt.description.splitlines()
        # timeRange = convert_chapter_format_to_start_end_format(parse_lines(desc_lines))
        generate_clips(file_path, time_range)

        input('Hit Enter to exit')

    # https://stackoverflow.com/questions/41529016/python-http-client-incomplete-read0-bytes-read-error
    except IncompleteRead as e:
        print("Error", e)

    except Exception as e:
        print("Error", e)  # to handle exception
        input('Hit Enter to exit')


if __name__ == "__main__":
    main()
