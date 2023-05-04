import unittest
from src.main.model.Course import Course
from src.main.constants import constant
from src.main.controller.implementation.RegisterCourseCmdExecutor import RegisterCourseCmdExecutor
from unittest.mock import patch
from io import StringIO
from unittest.mock import MagicMock

class TestRegisterCourseCmdExecutor(unittest.TestCase):

    def setUp(self):
        
        self.executor = RegisterCourseCmdExecutor()
        self.offeredCourse = Course("JAVA", "JAMES", "15062022", 1, 2)
        self.offeredCourse._set_course_status(constant.COURSE_CANCELED)
        self.coursesDet = {
            'OFFERING-JAVA-JAMES': self.offeredCourse
        }
        self.regIDvsCourse = {}

    @patch('sys.stdout', new_callable=StringIO)
    def test_executeCommand_registered_valid_data(self, mock_stdout):
        command_attributes = ['ANDY@GMAIL.COM', 'OFFERING-JAVA-JAMES']
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)
        
        command_attributes = ['WOO@GMAIL.COM', 'OFFERING-JAVA-JAMES']
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)

        expected_output = 'REG-COURSE-ANDY-JAVA ACCEPTED\nREG-COURSE-WOO-JAVA ACCEPTED\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_executeCommand_registered_course_full(self, mock_stdout):
        command_attributes = ['ANDY@GMAIL.COM', 'OFFERING-JAVA-JAMES']
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)
        
        command_attributes = ['WOO@GMAIL.COM', 'OFFERING-JAVA-JAMES']
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)

        command_attributes = ['JANE@GMAIL.COM', 'OFFERING-JAVA-JAMES']
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)

        expected_output = 'REG-COURSE-ANDY-JAVA ACCEPTED\nREG-COURSE-WOO-JAVA ACCEPTED\nCOURSE_FULL_ERROR\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_executeCommand_registered_invalid_data(self, mock_stdout):
        command_attributes = ['ANDY@GMAIL.COM', 'OFFERING-JAVA-JAMES']
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)
        
        command_attributes = ['JANE', 'OFFERING-JAVA-JAMES']
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)
        expected_output = 'REG-COURSE-ANDY-JAVA ACCEPTED\nINPUT_DATA_ERROR\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        # # Act
        # with self.assertRaises(SystemExit) as context:
        #     self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)

        # # Assert
        # self.assertEqual(context.exception.code, constant.INPUT_DATA_ERROR)

if __name__ == '__main__':
    unittest.main()
