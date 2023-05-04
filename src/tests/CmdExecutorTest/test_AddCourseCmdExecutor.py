import unittest
from unittest.mock import patch

from src.main.controller.implementation.AddCourseCmdExecutor import AddCourseCmdExecutor

from src.main.constants import constant
from src.main.model.Course import Course

class TestAddCourseCmdExecutor(unittest.TestCase):

    def setUp(self):
        self.cmd_executor = AddCourseCmdExecutor()

    def test_executeCommand_with_valid_data(self):
        # Prepare
        coursesDet = {}
        regIDvsCourse = {}
        command_attributes = ["JAVA", "JAMES", "15062022", 1, 2]
        expected_course_id = "OFFERING-JAVA-JAMES"

        # Execute
        course = self.cmd_executor.executeCommand(coursesDet, regIDvsCourse, command_attributes)

        # Assert
        self.assertIsInstance(course, Course)
        self.assertEqual(course._get_course_id(), expected_course_id)
        self.assertEqual(coursesDet[expected_course_id], course)

    def test_executeCommand_with_invalid_data(self):
        # Prepare
        coursesDet = {}
        regIDvsCourse = {}
        # no of params are not getting matched
        command_attributes = ["JAVA", "JAMES", "15062022", 1]

        # Execute
        with patch('builtins.print') as mocked_print:
            course = self.cmd_executor.executeCommand(coursesDet, regIDvsCourse, command_attributes)

        # Assert
        self.assertIsNone(course)
        mocked_print.assert_called_once_with(constant.INPUT_DATA_ERROR)

    def test_executeCommand_with_invalid_data(self):
        # Prepare
        coursesDet = {}
        regIDvsCourse = {}
        # no of params are not getting matched
        command_attributes = ["JAVA", "JAMES", "15062022", 1]

        # Execute
        with patch('builtins.print') as mocked_print:
            course = self.cmd_executor.executeCommand(coursesDet, regIDvsCourse, command_attributes)

        # Assert
        self.assertIsNone(course)
        mocked_print.assert_called_once_with(constant.INPUT_DATA_ERROR)

if __name__ == '__main__':
    unittest.main()
