import unittest
from unittest.mock import patch
from io import StringIO
from src.main.controller.FileReader import FileReader
from src.main.LMS.LearningManagementSystem import LearningManagementSystem
from src.main.model.Command import Command
from unittest.mock import patch, MagicMock
from src.main.enums.CommandType import CommandType
from src.main.CmdExecutorFactory.commandExecutorFactory import CommandExecutorFactory

from unittest import mock
class TestMain(unittest.TestCase):
    def test_integration(self):
        # Set up test data
        commands = [
            "ADD-COURSE-OFFERING PYTHON JOHN 05062022 1 3",
            "REGISTER WOO@GMAIL.COM OFFERING-PYTHON-JOHN",
            "REGISTER ANDY@GMAIL.COM OFFERING-PYTHON-JOHN",
            "REGISTER BOBY@GMAIL.COM OFFERING-PYTHON-JOHN",
            "CANCELREG-COURSE-BOBY-PYTHON",
            "ALLOTOFFERING-PYTHON-JOHN"
        ]
        expected_output = [
            "OFFERING-PYTHON-JOHN",
            "REG-COURSE-WOO-PYTHON ACCEPTED",
            "REG-COURSE-ANDY-PYTHON ACCEPTED",
            "REG-COURSE-BOBY-PYTHON ACCEPTED",
            "REG-COURSE-BOBY-PYTHON CANCEL_ACCEPTED",
            "REG-COURSE-ANDY-PYTHON ANDY@GMAIL.COM OFFERING-PYTHON-JOHN PYTHON JOHN 05062022 CONFIRMED\nREG-COURSE-WOO-PYTHON WOO@GMAIL.COM OFFERING-PYTHON-JOHN PYTHON JOHN 05062022 CONFIRMED"
        ]
        input_str = "\n".join(commands)
        expected_output_str = "\n".join(expected_output)

        self.filePath = "xyz.txt"
        with mock.patch('builtins.open', mock.mock_open(read_data='ADD-COURSE-OFFERING PYTHON JOHN 05062022 1 3\nREGISTER WOO@GMAIL.COM OFFERING-PYTHON-JOHN\n\n')):
            self.reader = FileReader(self.filePath)
        # Run main function with mocked data
        with patch('src.main.controller.FileReader.FileReader', return_value=self.reader), patch('sys.stdout', new=StringIO()) as mock_stdout:
            lms = LearningManagementSystem()
            command = MagicMock()
            command._get_command_type.return_value = CommandType.ADD_COURSE_OFFERING
            command._get_command_attributes.return_value = ["Course Title", "Instructor", "2023-04-16", 10, 20]
            cmdExec = MagicMock()
            cmdExec.executeCommand = MagicMock()
            CommandExecutorFactory.create_command = MagicMock(return_value=cmdExec)
            
            lms.runCommand(command)
            # TO DO
            # Test output
            # self.assertEqual(mock_stdout.getvalue().strip(), expected_output_str)

if __name__ == '__main__':
    unittest.main()


