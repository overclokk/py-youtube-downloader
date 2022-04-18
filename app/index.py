# import win32clipboard
# import argparse
import glob
import os

from pytube import YouTube
from pytube.cli import on_progress
from pytube.exceptions import VideoUnavailable
from pytube.streams import Stream

from utils.Downloader import Downloader
from utils.Menu import Menu
from utils.functions import generate_clips, convert_chapter_format_to_start_end_format, parse_lines

VIDEO_DIR_CONTAINER = 'video'


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


def download_video():
    url = input("Insert video link: ")
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
    except VideoUnavailable:
        print(f'Video {url} is unavailable, skipping.')
    else:
        downloader: Downloader = Downloader(yt)
        downloader.in_dir(VIDEO_DIR_CONTAINER).download()


# Gets a single clip from video
def create_clip_from_cli_arguments() -> None:
    def on_complete(stream: Stream, file_handle: str):
        time_range = [input("Insert clip time range [HH:]MM:SS,[HH:]MM:SS: ").split(',')]
        generate_clips(file_handle, time_range)

    url = input("Insert video link: ")
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
    except VideoUnavailable:
        print(f'Video {url} is unavailable, skipping.')
    else:
        yt.register_on_complete_callback(on_complete)
        downloader: Downloader = Downloader(yt)
        downloader.in_dir(VIDEO_DIR_CONTAINER).download()


def create_clips_from_video_chapters() -> None:
    url = input("Insert video link: ")
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
    except VideoUnavailable:
        print(f'Video {url} is unavailable, skipping.')
    else:
        downloader: Downloader = Downloader(yt)
        file_path = downloader.in_dir(VIDEO_DIR_CONTAINER).download()
        desc_lines = yt.description.splitlines()
        time_range = convert_chapter_format_to_start_end_format(parse_lines(desc_lines))
        generate_clips(file_path, time_range)


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


if __name__ == "__main__":
    main()
