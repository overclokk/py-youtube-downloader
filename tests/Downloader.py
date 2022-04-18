import unittest
from unittest.mock import Mock

from app.utils.Downloader import Downloader


class DownloaderTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.__youtube = Mock()

    def __get_instance(self) -> Downloader:
        sut = Downloader(self.__youtube)
        return sut

    def test_instance_ok(self):
        sut = self.__get_instance()
        self.assertIsInstance(sut, Downloader)

    def test_add_dir_name(self):
        sut = self.__get_instance()
        sut.in_dir('video')

    # def test_download(self):
    #     sut = self.__get_instance()
    #     sut.in_dir('video').download()


if __name__ == '__main__':
    unittest.main()
