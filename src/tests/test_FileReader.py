import unittest
from src.main.controller.CommandExtractor import CommandExtractor
from src.main.controller.FileReader import FileReader
from unittest.mock import MagicMock
from unittest import mock



class TestFileReader(unittest.TestCase):
    def setUp(self):
        # # create a mock file object
        self.mock_file = MagicMock()
        self.reader = None
        self.filePath = "sample.txt"
        with mock.patch('builtins.open', mock.mock_open(read_data='ADD-COURSE-OFFERING PYTHON JOHN 05062022 1 3\nREGISTER WOO@GMAIL.COM OFFERING-PYTHON-JOHN\n\n')):
            self.reader = FileReader(self.filePath)
        
    def test_check_extension_txt_file(self):
        result = self.reader.check_extension(self.filePath)
        self.assertTrue(result)

    def test_check_extension_non_txt_file(self):
        result = self.reader.check_extension("test.docx")
        self.assertFalse(result)

    def test_iterate_over_file(self):
        expected_commands = [
            CommandExtractor().extract_command("ADD-COURSE-OFFERING PYTHON JOHN 05062022 1 3\n"),
            CommandExtractor().extract_command("REGISTER WOO@GMAIL.COM OFFERING-PYTHON-JOHN\n"),
        ]
        for expected in expected_commands:
            actual = next(self.reader)
            self.assertEqual(expected._get_command_type(), actual._get_command_type())
            self.assertEqual(expected._get_command_attributes(), actual._get_command_attributes())
        self.assertIsNone(next(self.reader))


