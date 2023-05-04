import unittest
from src.main.CmdExecutorFactory.commandExecutorFactory import CommandExecutorFactory
from src.main.enums.CommandType import CommandType
from src.main.model.Command import Command
from src.main.controller.CommandExtractor import CommandExtractor

class TestCommandExtractor(unittest.TestCase):

    def setUp(self):
        self.commandExtractor = CommandExtractor()

    def test_extract_command_valid_input(self):
        input_line = "ADD-COURSE-OFFERING PYTHON JOHN 05062022 1 3"
        expected_command = Command()
        expected_command._set_command_type("ADD-COURSE-OFFERING")
        expected_command._set_command_attributes("PYTHON")
        expected_command._set_command_attributes("JOHN")
        expected_command._set_command_attributes("05062022")
        expected_command._set_command_attributes("1")
        expected_command._set_command_attributes("3")

        command = self.commandExtractor.extract_command(input_line)

        self.assertEqual(command._get_command_type(), expected_command._get_command_type())
        self.assertEqual(command._get_command_attributes(), expected_command._get_command_attributes())

    def test_extract_command_invalid_input(self):
        input_line = "ADD-COURSE-OFFERING PYTHON JOHN 05062022 1"
        expected_command = Command()

        command = self.commandExtractor.extract_command(input_line)

        self.assertEqual(command._get_command_type(), expected_command._get_command_type())
        self.assertEqual(command._get_command_attributes(), expected_command._get_command_attributes())
