# import win32clipboard
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
    parser.add_argument("-v", "--video", help="Link of the video to download", required=True)
    parser.add_argument("-c", "--cut", help="Timestamp range to cut", required=True)
    # parser.add_argument("--clipboard", help="Copies video link from clipboard")
    # parser.add_argument("--file", help="Gets video and timestamps from a file")

    args = parser.parse_args();
    getClip(args.video, args.cut)
    

# Downloads a video and generates a clip based on the timestamp range given
def getClip(videoURL, timeRange):
    try:
        #where to save
        SAVE_PATH = "video"

        yt = YouTube( videoURL )
        timeCuts = getTimestamps(timeRange)
        print( 'Title :', yt.title )
        # print('Available formats :')
        # for stream in yt.streams.all():
        # print(stream)

        # itag = input('\nEnter the itag number to download video of that format: ')
        # stream = yt.streams.get_by_itag( itag )
        stream = yt.streams.get_highest_resolution()

        print( '\nDownloading--- ' + yt.title + ' into location : ' + SAVE_PATH )
        stream.download( SAVE_PATH )

        print( stream.default_filename )
        input_video_path = stream.default_filename

        ffmpeg_extract_subclip( SAVE_PATH + os.path.sep + input_video_path, int(timeCuts[0]), int(timeCuts[1]), targetname="clip.mp4")

        input('Hit Enter to exit')
    except Exception as e:
        print("Error",e) #to handle exception
        input('Hit Enter to exit')

# Separates timestamp range
def getTimestamps(timeRange):
    return timeRange.rsplit(":")


if __name__ == "__main__":
    main()