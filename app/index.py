# import win32clipboard
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import os

# https://superuser.com/questions/1567253/how-to-download-chapters-of-a-youtube-video-as-separate-video-files
link = "https://www.youtube.com/watch?v=2sPcpOhAK64"

# https://medium.com/daily-python/python-script-to-download-youtube-videos-daily-python-6-c3788be5b6b1
# try:
#     # get clipboard data
#     win32clipboard.OpenClipboard()
#     link = win32clipboard.GetClipboardData()
#     win32clipboard.CloseClipboard()
# except Exception as ex:
#     print('Error : ', ex )
#     exit()


try:
    #where to save
    SAVE_PATH = "video"

    yt = YouTube( link )
    print( 'Title :', yt.title )

#     print('Available formats :')
#     for stream in yt.streams.all():
#         print(stream)

#     itag = input('\nEnter the itag number to download video of that format: ')
#     stream = yt.streams.get_by_itag( itag )
    stream = yt.streams.get_highest_resolution()

    print( '\nDownloading--- ' + yt.title + ' into location : ' + SAVE_PATH )
    stream.download( SAVE_PATH )

    print( stream.default_filename )
    input_video_path = stream.default_filename

    ffmpeg_extract_subclip( SAVE_PATH + os.path.sep + input_video_path, 4380, 4699, targetname="clip.mp4")

    input('Hit Enter to exit')
except Exception as e:
    print("Error",e) #to handle exception
    input('Hit Enter to exit')