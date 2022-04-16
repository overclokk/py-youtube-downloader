import unittest

from app.utils.functions import get_seconds, parse_file, convert_chapter_format_to_start_end_format


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
        self.assertEqual(3, len(file_content), '')

    def test_get_timestamps_from_file_with_chapters_format(self):
        file_content = parse_file('fixtures/chapters.txt')
        self.assertEqual(
            [['0:00'], ['00:00'], ['00:15'], ['00:16'], ['00:17'], ['00:18'], ['00:19']],
            file_content,
            ''
        )
        self.assertEqual(7, len(file_content), '')

    def test_format_conversion(self):
        actual = [['00:15'], ['00:16'], ['00:17'], ['00:18'], ['00:19']]
        expected = [['00:15', '00:16'], ['00:16', '00:17'], ['00:17', '00:18'], ['00:18', '00:19']]

        converted = convert_chapter_format_to_start_end_format(actual)
        self.assertEqual(expected, converted, '')

    def test_video_finder(self):
        content = [
            '33 parte 2.txt', 'Era evitabile il conflitto_ Con V.E. Parsi.mp4',
            'index.py',
            'La Scuola Oltre Le Illusioni CONVEGNO sabato 9 aprile.mp4',
            "Storia dell'Ucraina conoscere il contesto per capire la guerra.txt"
        ]

        video_list = []
        for file in content:
            if file.find('.mp4') < 1:
                continue
            video_list.append( file )

        print(video_list)


if __name__ == '__main__':
    unittest.main()
