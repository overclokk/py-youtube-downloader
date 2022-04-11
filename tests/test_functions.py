import unittest

from app.functions import get_seconds, parse_file


class FunctionsTestCase(unittest.TestCase):
    def test_get_seconds(self):
        seconds: int = get_seconds('1:05:55')
        self.assertEqual(3955, seconds)
        seconds: int = get_seconds('05:55')
        self.assertEqual(355, seconds)
        seconds: int = get_seconds('1:5')
        self.assertEqual(65, seconds)
        seconds: int = get_seconds('0:5')
        self.assertEqual(5, seconds)

    def test_get_timestamps_from_file_with_timestamp_format(self):
        file_content = parse_file('fixtures/timestamps.txt')
        self.assertEqual(
            [['15:20', '18:00'], ['15:20', '18:00'], ['15:20', '18:00']],
            file_content,
            ''
        )
        self.assertEqual(3,len(file_content),'')

    def test_get_timestamps_from_file_with_chapters_format(self):
        file_content = parse_file('fixtures/chapters.txt')
        self.assertEqual(
            [['00:15'], ['00:15'], ['00:15'], ['00:15'], ['00:15']],
            file_content,
            ''
        )
        self.assertEqual(5, len(file_content), '')


if __name__ == '__main__':
    unittest.main()
