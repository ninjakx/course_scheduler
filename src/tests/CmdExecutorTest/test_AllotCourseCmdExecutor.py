import unittest
from src.main.model.Employee import Employee
from src.main.model.Course import Course
from src.main.constants import constant
from unittest.mock import patch
from src.main.controller.implementation.AllotCourseCmdExecutor import AllotCourseCmdExecutor
from io import StringIO

class TestAllotCourseCmdExecutor(unittest.TestCase):

    def setUp(self):
        
        self.executor = AllotCourseCmdExecutor()
        self.offeredCourse = Course("JAVA", "JAMES", "15062022", 1, 2)
        self.emp = Employee("WOO@GMAIL.COM")
        self.offeredCourse._register_employee(self.emp)
        self.offeredCourse._set_course_status(constant.COURSE_CANCELED)
        self.offeredCourse._set_course_id("OFFERING-JAVA-JAMES")
        self.coursesDet = {
            'OFFERING-JAVA-JAMES': self.offeredCourse
        }
        self.regIDvsCourse = {'REG-COURSE-WOO-JAVA': self.offeredCourse}

    @patch('sys.stdout', new_callable=StringIO)
    def test_executeCommand_with_course_allocated(self, mock_stdout):
        command_attributes = ['OFFERING-JAVA-JAMES']

        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)

        expected_output = 'REG-COURSE-WOO-JAVA WOO@GMAIL.COM OFFERING-JAVA-JAMES JAVA JAMES 15062022 CONFIRMED\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_executeCommand_with_course_full_error(self, mock_stdout):
        self.maxDiff = None
        command_attributes = ['OFFERING-JAVA-JAMES']

        self.emp = Employee("ANDY@GMAIL.COM")
        self.offeredCourse._register_employee(self.emp)
        self.emp = Employee("ZAYNE@GMAIL.COM")
        # won't get registered as course size exceeded in registration time
        self.regIDvsCourse = {'REG-COURSE-ANDY-JAVA': self.offeredCourse,
                              'REG-COURSE-WOO-JAVA': self.offeredCourse}

        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)
        expected_output = 'REG-COURSE-ANDY-JAVA ANDY@GMAIL.COM OFFERING-JAVA-JAMES JAVA JAMES 15062022 CONFIRMED\nREG-COURSE-WOO-JAVA WOO@GMAIL.COM OFFERING-JAVA-JAMES JAVA JAMES 15062022 CONFIRMED\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()


