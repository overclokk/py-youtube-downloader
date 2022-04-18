import os

from pytube import YouTube
from http.client import IncompleteRead


class Downloader:
    __yt: YouTube
    __file_path: str
    __in: str

    def __init__(self, yt_obj: YouTube) -> None:
        self.__yt = yt_obj
        self.__file_path = ''
        self.__in = ''

    def in_dir(self, _in: str):
        self.__in = _in
        return self

    def download(self) -> str:
        try:
            stream = self.__yt.streams.get_highest_resolution()
            self.__file_path = self.__in + os.path.sep + stream.default_filename
            print('\nDownloading--- ' + self.__yt.title + ' into location : ' + self.__file_path)
            stream.download(self.__in)

            return self.__file_path

        # https://stackoverflow.com/questions/41529016/python-http-client-incomplete-read0-bytes-read-error
        except IncompleteRead as e:
            print("Error", e)

        except Exception as e:
            print("Error", e)  # to handle exception
            input('Hit Enter to exit')
