import unittest

from app.functions import get_seconds


class FunctionsTestCase(unittest.TestCase):
    def test_get_seconds(self):
        seconds = get_seconds('1:05:55')
        self.assertEqual(seconds, 3955)
        seconds = get_seconds('05:55')
        self.assertEqual(seconds, 355)
        seconds = get_seconds('1:5')
        self.assertEqual(seconds, 65)
        seconds = get_seconds('0:5')
        self.assertEqual(seconds, 5)


if __name__ == '__main__':
    unittest.main()
